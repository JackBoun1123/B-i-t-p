<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Trang chủ</title>
    <link rel="stylesheet" href="layout/css/styleDK.css?v=5">
</head>

<body>
    <div class="container">
        <header>
            <h1>BENNIS SUPERCARS STORE <img style="border-radius:100px; position:absolute; top:35px;"src="upload/sanpham/tick.jpg" width="20px"></h1>
        </header>
        <aside>
            <h2 style="    font-size: xx-large;">Menu</h2>
            <a href="#">
                <ul>
                    <a href="index.php?page=trangchu">
                        <li><b>Trang chủ</b></li>
                    </a>
                    <a href="index.php?page=dangky">
                        <li><b>Đăng ký</b></li>
                    </a>
                    <a href="index.php?page=login">
                        <li>
                            <?php
                                if(isset($_COOKIE["dangnhap"]))
                                {
                                    echo    "<b><a href='index.php?page=logout'>Đăng xuất</a></b>";
                                }
                                else
                                {
                                    echo    "<b><a href='index.php?page=login'>Đăng nhập</a></b>";
                                }
                            ?>
                        </li>
                    </a>
                    <a href="index.php?page=congty">
                        <li><b>Công ty</b></li>
                    </a>
                    <a href="index.php?page=sanpham">
                        <li><b>Sản phẩm</b></li>
                    </a>
                    <?php
                    $obj = new database(); // ten class
                    $loaisp=$obj->xuatdulieu("select distinct brand from supercars"); // goi phuong thuc  xuat du lieu
                    if($loaisp)
                    {
                        for($i=0;$i<count($loaisp);$i++) // hien tat ca du lieu ra
                        {
                            echo    "<ul>";
                            echo '<a style="color:gray;" href="index.php?page=sanpham&cate='.$loaisp[$i]['brand'].'"><li>'.$loaisp[$i]['brand'].'</li></a>';
                            echo "</ul>";
                        }
                    }

                    ?>
                </ul>
            </a>
            <a href=""></a>
        </aside>
        <section>
