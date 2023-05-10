import chessvision
import cv2

board_extractor, piece_classifier = chessvision.load_models()
fi=0
print(board_extractor,piece_classifier)
for i in range(0,250):
    for j in range(0,5):
        try:
            img = cv2.imread(f"D:\Python\PDFToTactics\Individuals\Tactics_{i}_part{j}.png")

            board_img, mask, predictions, chessboard, FEN, squares, names = chessvision.classify_raw(img, board_model=board_extractor, sq_model=piece_classifier)

            if FEN != '8/8/8/8/8/8/8/8':
                print(f"Predicted FEN: {FEN}")
                fi+=1
        except Exception as e:
            continue
print(fi)