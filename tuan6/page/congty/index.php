<?php
    include('class/clscongty.php');
    $obj =  new congty();
    include('page/congty/xuly.php');
    $sanpham= $obj->danhsachsanpham();
    if ($sanpham)
    {
        echo '<form action="" method="post">
        <table border="1px" style="border-collapse:collapse;">
            <tr>
                <th>STT</th>
                <th>Tên hãng</th>
                <th>Model</th>
                <th>Giá</th>
                <th>Năm sản xuất</th>
                <th>Ảnh</th>
                <th>Thao tác</th>
            </tr>';
            for ($i= 0; $i<count($sanpham); $i++)
            {
                echo '
                <tr>
                    <td align="center">'.($i+1).'</td>
                    <td align="center"><a style="color: white;" href="index.php?page=sanpham&cate='.$sanpham[$i]["brand"].'">'.$sanpham[$i]["brand"].'</a></td>
                    <td align="center"><a style="color: white;" href="index.php?page=detail&item='.$sanpham[$i]["car_id"].'">'.$sanpham[$i]["model"].'</td>
                    <td align="center">'.number_format($sanpham[$i]["price"]).'$</td>
                    <td align="center">'.$sanpham[$i]["year"].'</td>
                    <td align="center"><img width="60px"src="upload/sanpham/'.$sanpham[$i]["img"].'" alt=""></td>
                    <td align="center">
                        <button onclick="return confirm(\'Bạn có chắc muốn xóa '.$sanpham[$i]["model"].' ?\')"  type="submit" value="'.$sanpham[$i]["car_id"].'" name="delete">Xóa</button>
                        <button onclick="return confirm(\'Sửa sản phẩm '.$sanpham[$i]["model"].' chứ?\')"  type="submit" value="'.$sanpham[$i]["car_id"].'" name="update">Sửa</button>
                    </td>
                </tr>';
            }
        echo '</table>
        </form>';
    }

?>






