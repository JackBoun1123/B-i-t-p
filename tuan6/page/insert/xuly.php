<?php
session_start();
    if (isset($_POST['upload']))
    {  
        if(isset($_SESSION['login']))
        {
        $brand = $_POST['brand'];
       $model = $_POST['model'];
       $price = $_POST['price'];
       $year = $_POST['year'];
       $img = $_FILES['img'];
       $directory = 'upload/sanpham/';
       $path = $directory.rand(0,1000).basename($img['name']);
       move_uploaded_file($img['tmp_name'], $path);
        $sql = 'Insert into supercars (brand, model, price, year, img)
                Values ("'.$brand.'","'.$model.'",'.$price.','.$year.',"'.$img['name'].'");
                ';
        $obj->thucthi( $sql);
        echo'<script>alert("Cập nhật thành công");</script>';
        }
        else
        {
            echo '<script>alert("Bạn cần đăng nhập để có thể đăng tải sản phẩm!");setTimeout(function(){window.location.href = "index.php?page=login";}, 0);</script>';
        }
    }
?>
