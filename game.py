import requests
from bs4 import BeautifulSoup
from collections import deque
import time
import networkx as nx
import matplotlib.pyplot as plt
import aiohttp
import asyncio


class WikipediaHitlerGame:
    def __init__(self, start_url, target_keyword, max_depth):
        self.start_url = start_url
        self.target_keyword = target_keyword
        self.max_depth = max_depth
        self.visited_links = set()
        self.session = aiohttp.ClientSession()

    async def parse_article(self, url):
        async with self.session.get(url) as response:
            html = await response.text()

        soup = BeautifulSoup(html, 'html.parser')
        body_content = soup.find(id="bodyContent")

        if not body_content:
            return []

        links = body_content.find_all('a', href=True)

        article_links = []
        for link in links:
            article_link = link['href']
            if article_link.startswith('/wiki/') and ':' not in article_link:
                article_links.append(article_link.split('/')[-1])

        return article_links

    async def play_game(self):
        start_time = time.time()
        queue = deque([(self.start_url, 0, [])])

        while queue:
            current_url, current_depth, path = queue.popleft()

            if current_url in self.visited_links:
                continue
            if current_depth >= self.max_depth:
                return None

            print(f"Analyzing {current_url, current_depth}")
            self.visited_links.add(current_url)

            article_links = await self.parse_article(f"https://en.wikipedia.org/wiki/{current_url}")
            for link in article_links:
                if link == self.target_keyword:
                    end_time = time.time()
                    elapsed_time = end_time - start_time

                    return path + [current_url, link, elapsed_time]

                queue.append((link, current_depth + 1, path + [current_url]))
            # print(queue,"\n")
        return None

    async def close_session(self):
        await self.session.close()

    async def create_graph(self, result_path, limit_data_per_depth_in_graph):
        G = nx.MultiGraph()
        article_links_dict = {}
        colors = ["#f44336", "#ff9800", "#ffc107", "#8bc34a", "#00d4ce", "#9656ce"]

        G.add_node(result_path[0])
        G.add_node(result_path[1])
        G.add_node(result_path[2])
        for idx, url in enumerate(result_path[:-2]):
            article_links = await self.parse_article(f"https://en.wikipedia.org/wiki/{url}")
            limited_article_links = article_links[:limit_data_per_depth_in_graph]
            article_links_dict[url] = limited_article_links
            G.add_nodes_from(limited_article_links)
            for link in limited_article_links:
                G.add_edge(url, link)
            G.add_edge(url, result_path[idx + 1])
            # for i in article_links_dict[url]:
            #     nx.draw_networkx_nodes(G, pos, nodelist=[i], node_color=colors[idx+1], alpha=0.5)

        pos = nx.spring_layout(G, k=0.2, scale=100)
        plt.title(f"Shortest way from {result_path[0]} to {result_path[-2]}")

        nx.draw(G, pos, with_labels=True, node_size=0, font_size=9, font_color='black', font_weight='bold', edge_color='gray')

        for idx, url in enumerate(result_path[:-2]):
            for i in article_links_dict[url]:
                nx.draw_networkx_nodes(G, pos, nodelist=[i], node_color=colors[idx + 1], alpha=0.6, node_size=700)

        for i in range(len(result_path) - 1):
            nx.draw_networkx_nodes(G, pos, nodelist=[result_path[i]], node_color=colors[i], node_size=1700)

        for i in range(len(result_path) - 2):
            nx.draw_networkx_edges(G, pos, edgelist=[(result_path[i], result_path[i + 1])], edge_color=colors[i], width=6)


        plt.show()