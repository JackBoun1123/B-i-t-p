<?php
session_start();
$login=$_SESSION['login'];
$obj = new database();
$sql="select * from supercars s join inventory i on s.car_id = i.car_id where s.car_id='$item'";
$sanpham=$obj->xuatdulieu($sql);
if($sanpham)
    {
    for($i=0;$i<count($sanpham);$i++) 
        {
            $quantity =$sanpham[$i]['quantity'];
            echo "<div class='detail'>
                <h2 style='background-color: orange;color: white;font-size: xx-large;'>CHI TIẾT SẢN PHẨM</h2><br>
                <div class='info'>
                    <br>
                    <h1>".$sanpham[$i]['model']."</h1>
                    <br><b>Hãng: </b>".$sanpham[$i]['brand']." <br>
                    <br> <b>Sản xuất năm: </b>".$sanpham[$i]['year']."<br>
                    <br> <b>Giá: </b>".number_format($sanpham[$i]['price'])."$ <br>
                    <br><b>Số lượng: </b><input type='number' name='quantity' style='width:80px;' min='1' max='$quantity'> <br>
                    <br><b>Màu sắc:</b>  
                    <button style='border-radius:15px;' name='color' value='pink'><img style='border-radius:10px;'height=18px width=20px src='upload/sanpham/pink.png' alt='hồng'></button>
                    <button style='border-radius:15px;' name='color' value='gold'><img style='border-radius:10px;'height=18px width=20px src='upload/sanpham/gold.jpg' alt='vàng'></button>
                    <button style='border-radius:15px;' name='color' value='wine'><img style='border-radius:10px;'height=18px width=20px src='upload/sanpham/darkwine.jpg' alt='rượu'></button>

                    ";
                    if (isset($login) && $login == true) {
                        echo "<br><button name='order' >Đặt hàng</button><br>";
                    } else {
                        echo "<br><a href='index.php?page=login'><button>Đăng nhập để đặt hàng</button></a><br>";
                    }
                    echo"
                    <br><a href='index.php?page=sanpham&cate=".$sanpham[$i]['brand']."' style='text-align:center; color:green;'>Tiếp tục mua sắm</a>
                </div>
                <div class='hinh'><img src='upload/sanpham/".$sanpham[$i]['img']."'></div>
            </div>";
        }
    }
else
    echo "<script>alert('Sản phẩm đã hết, vui lòng chọn sản phẩm khác!');setTimeout(function(){window.location.href = 'index.php?page=sanpham';}, 0);</script>";
?>
<div style="clear:both"></div>


