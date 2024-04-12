<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<?php
    $name = $_POST["hoTen"];
    $hometown = $_POST["queQuan"];
    $email = $_POST["email"];
    $phone = $_POST["dienThoai"];
    $pass = md5($_POST["password"]);
    if ($obj ->themtaikhoan($name, $hometown, $email, $phone, $pass))
        echo "<script>alert('Tài khoản đã đăng ký thành công!')</script>";
    else
        echo "<script>alert('Đăng ký thất bại!')</script>";

    
?>
</body>
</html>