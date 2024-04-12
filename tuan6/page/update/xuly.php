<?php
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
       $path = $directory.basename($img['name']);
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
    if (isset($_POST['delete']))
    {
        $choose = $_POST['choose'];
        $sql = "DELETE FROM supercars WHERE car_id = '".$choose."'";
        $obj->thucthi($sql);
    }
    if (isset($_POST["update"]))
    {
        $offer = array('brand', 'model', 'price', 'year', 'img');
        foreach ($offer as $i) {
            if($_POST["u".$i]!=null)
            {
                $sql = "UPDATE supercars SET ".$i."='".$_POST["u".$i]."' WHERE car_id='".$_POST['choose']."'";
                echo $sql;
            }
        }
        if(isset($_FILES['uimg'])){
            $img = $_FILES['uimg']['name'];
            $directory = "upload/sanpham/";
            $path = $directory . basename($_FILES["uimg"]["name"]);
            if(move_uploaded_file($_FILES['uimg']['tmp_name'],$path)){
                $sql = "UPDATE supercars SET img='".$img['name']."' WHERE car_id='".$_POST['choose']."'";
                echo $sql;
            }else{
                echo "Failed to upload image";
            }
        }
    }
    else
        echo '<script>alert('.$sql.');setTimeout(function(){window.location.href = "index.php?page=login";}, 0);</script>';


?>