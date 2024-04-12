<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
<form action="" method="Post" enctype="multipart/form-data">
        <table>
            <tr>
                <td></td>
                <td><h1>Cập nhật sản phẩm</h1></td>
            </tr>
            <tr>
                <td>
                    Chọn sản phẩm cần cập nhật:
                </td>
                <td>
                <select onchange="getCarID(this.value)">
                        <?php
                        $id=$_SESSION['id_car_update'];
                        $sql= "Select * from  supercars where car_id='$id'";
                        $sanpham = $obj->xuatdulieu($sql);
                        echo " <option value='".$sanpham[0]['car_id']."'>".$sanpham[0]['car_id']." ".$sanpham[0]['brand']." ".$sanpham[0]['model']."</option>";
                        $brand = $sanpham[0]['brand'];
                        $model = $sanpham[0]['model'];
                        $price = $sanpham[0]['price'];
                        $year = $sanpham[0]['year'];
                        $img = $sanpham[0]['img'];
                        $sql= 'Select * from  supercars';
                        $sanpham = $obj->xuatdulieu($sql);
                        for ($i=0; $i<count($sanpham); $i++)
                        {
                            echo " <option value='".$sanpham[$i]['car_id']."'>".$sanpham[$i]['car_id']." ".$sanpham[$i]['brand']." ".$sanpham[$i]['model']."</option>";
                        }
                        ?>
                    </select>     
                    <div id="div1">
                    <?php
                        echo '
                        <tr>
                            <td>Tên hãng:</td>
                            <td><input type="text" name="ubrand" value="'.$brand.'" ></td>
                        </tr>
                        <tr>
                            <td>Tên Model:</td>
                            <td><input type="text" name="umodel" value="'.$model.'" ></td>
                        </tr>
                        <tr>
                            <td>Giá bán:</td>
                            <td><input type="money" name="uprice" value="'.$price.'"></td>
                        </tr>
                        <tr>
                            <td>Năm sản xuất:</td>
                            <td><input type="number" id="year" name="uyear" min="1996" value="'.$year.'">
                                <script>
                                    var today = new Date();
                                    var year = today.getFullYear();
                                    document.getElementById("year").max = year;
                                </script>
                        </td>
                        </tr>
                        <tr>
                            <td>Ảnh sản phẩm:</td>
                            <td><input type="file" name="uimg" value="null" value="<img src="upload/sanpham/'.$img.'" alt="">"></td>
                        </tr>';
                    ?>
                    </div>
                </td>
            </tr>

            <tr>
                <td></td>
                <td>
                    <input type="submit" name="update" value="Cập nhật">
                    <input type="reset" value="Làm lại">
                </td>
            </tr>
        </table>
    </form>
    </body>
</html>

<script>
    function getCarID(value) {
        $.ajax({
            url: "ajax.php",
            type: 'POST',
            data: 'value=' + value,
            success: function(result) {
                $("#div1").html(result);
            }
        });
    }
</script>
<div style="clear:both"></div>