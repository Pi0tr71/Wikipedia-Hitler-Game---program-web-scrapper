import asyncio
from game import WikipediaHitlerGame

if __name__ == "__main__":
    start_url = "Pinniped"
    target_keyword = "Adolf_Hitler"
    max_depth = 3  # for example Pinniped depth:0, Chattian depth:1, Austria depth:2, Adolf_Hitler depth:3 ~90 seconds
    limit_data_per_depth_in_graph = 30

    wikipedia_game = WikipediaHitlerGame(start_url, target_keyword, max_depth)
    loop = asyncio.get_event_loop()
    result_path = loop.run_until_complete(wikipedia_game.play_game())

    if result_path:
        print("Shortest path found:")
        for idx, link in enumerate(result_path[:-1]):
            print(f"{idx + 1}. {link}")
        print(f"Elapsed Time: {result_path[-1]:.2f} seconds")
        loop.run_until_complete(wikipedia_game.create_graph(result_path, limit_data_per_depth_in_graph))
    else:
        print(f"No path found in max {max_depth} depth.")


    loop.run_until_complete(wikipedia_game.close_session())
    loop.close()

