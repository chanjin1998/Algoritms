select concat("/home/grep/src/",ugb.board_id,"/",file_id,file_name,file_ext) as FILE_PATH from used_goods_board as ugb join used_goods_file as ugf
on ugb.board_id = ugf.board_id
WHERE VIEWS = (SELECT MAX(VIEWS) FROM USED_GOODS_BOARD)
order by file_id desc