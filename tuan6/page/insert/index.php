<?php
    include('class/clscongty.php');
    $obj =new congty();
    include('page/insert/xuly.php');
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Công ty</title>
</head>
<body>
    <form action="" method="post" enctype="multipart/form-data">
        <table>
            <tr>
                <td></td>
                <td><h1>Đăng tải sản phẩm mới</h1></td>
            </tr>
            <tr>
                <td>Tên hãng:</td>
                <td><input type="text" name="brand" required></td>
            </tr>
            <tr>
                <td>Tên Model:</td>
                <td><input type="text" name="model"  required></td>
            </tr>
            <tr>
                <td>Giá bán:</td>
                <td><input type="money" name="price"required></td>
            </tr>
            <tr>
                <td>Năm sản xuất:</td>
                <td><input type="number" id="year" name="year" min="1996"required>
                    <script>
                        var today = new Date();
                        var year = today.getFullYear();
                        document.getElementById('year').max = year;
                    </script>
            </td>
            </tr>
            <tr>
                <td>Ảnh sản phẩm:</td>
                <td><input type="file" name="img"required></td>
            </tr>
            <tr>
                <td></td>
                <td>
                    <input type="submit" name="upload" value="Đăng tải">
                    <input type="reset" value="Làm lại">
                </td>
            </tr>   
        </table>
    </form>
    </body>
</html>
