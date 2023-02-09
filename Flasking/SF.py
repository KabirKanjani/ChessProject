from stockfish import Stockfish

stockfish = Stockfish(path="D:\Download\stockfish_15.1_win_x64_avx2\stockfish_15.1_win_x64_avx2\stockfish-windows-2022-x86-64-avx2.exe")
stockfish.update_engine_parameters({"Hash": 2048, "UCI_Chess960": "true"}) # Gets stockfish to use a 2GB hash table, and also to play Chess960.

stockfish.set_fen_position("q2N2K1/2r3P1/1n5p/3p4/4p3/rP3p2/3k1PN1/7B w - - 0 1")

print(stockfish.get_best_move())
print(stockfish.get_top_moves(3))