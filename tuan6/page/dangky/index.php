<?php
    session_start();
    if (isset($_POST["log"])) {
        include_once("class/clscongty.php");
        $obj = new congty();
        include_once("page/dangky/xuly.php");
        header("Location: index.php?page=login");
    }
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="" method="POST">
        <table>
            <tr>
                <td></td>
                <td><b><span>THÔNG TIN ĐĂNG KÝ</span></b></td>
            </tr>
            <tr>
                <td id="red-text">Thông tin tài khoản</td>
                <td></td>
            </tr>
            <tr>
                <td>Email</td>
                <td><input type="text" name="email" id=""required></td>
            </tr>
            <tr>
                <td>Password</td>
                <td><input type="password" name="password" id=""required></td>
            </tr>
            <tr>
                <td>Nhập lại password</td>
                <td><input type="password" name="repassword" id=""required></td>
            </tr>
            <tr>
                <td id="red-text">Thông tin cá nhân</td>
                <td></td>
            </tr>
            <tr>
                <td>Họ tên</td>
                <td><input type="text" name="hoTen" id=""required></td>
            </tr>
            <tr>
                <td>Quê quán</td>
                <td><select name="queQuan"required>
                        <option selected disabled>Chọn Tỉnh/ Thành Phố</option>
                        <option value="Thành phố Hồ Chí Minh">Thành phố Hồ Chí Minh</option>
                        <option value="Hà Nội">Hà Nội</option>
                        <option value="Đà Nẵng">Đà Nẵng</option>
                        <option value="Khác">Khác</option>
                    </select></td>
            </tr>
            <tr>
                <td>Điện thoại</td>
                <td><input type="text" name="dienThoai" id=""required></td>
            </tr>
            <tr>
                <td>Giới tính</td>
                <td><input type="radio" name="gioiTinh" id="" value="Nam"> Nam
                    <input type="radio" name="gioiTinh" id="" value="Nữ"> Nữ
                </td>
            </tr>
            <tr>
                <td>Sở thích</td>
                <td><input type="checkbox" name="soThich[]" id="" value="Màu xanh"> Màu xanh
                    <input type="checkbox" name="soThich[]" id="" value="Màu đỏ"> Màu đỏ
                    <input type="checkbox" name="soThich[]" id="" value="Đồng quê"> Đồng quê
                    <input type="checkbox" name="soThich[]" id="" value="Cao nguyên"> Cao nguyên
                </td>
            </tr>
            <tr>
                <td></td>
                <td><input type="submit" value="Đăng ký" id="btn-dangKy" name="log"> <input type="button"
                        value="Làm lại">
                </td>
            </tr>
        </table>
    </form>
</body>
</html>

