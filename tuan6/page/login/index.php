<?php
    if (isset($_COOKIE["dangnhap"]))
        header("Location: index.php?page=trangchu");
    else
    {
        if (isset($_POST['login']))
        {
            include_once('class/clscongty.php');
            $obj =  new congty();
            include('page/login/xuly.php');
        }
    }
?>
<form action="" method="POST">
                <table>
                    <tr>
                        <td></td>
                        <th style = 'position: relative; right: 50px;'>THÔNG TIN ĐĂNG NHẬP</th>
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
                        <td></td>
                        <td><input type="checkbox" name> Nhớ thông tin đăng nhập</td>
                    </tr>
                    <tr>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td></td>
                        <td><input type="submit" value="Đăng nhập" id="btn-dangNhap" name="login"> <input
                                type="button" value="Làm lại">
                        </td>
                    </tr>
                </table>
            </form>