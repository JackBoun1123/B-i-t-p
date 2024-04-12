<?php
include('class/clsdatabase.php');
$obj= new database;
if(isset($_POST["value"]))
{
    $id=$_POST["value"];
    $sql= "Select * from  supercars where car_id='$id'";
    $sanpham = $obj->xuatdulieu($sql);
    $brand = $sanpham[0]['brand'];
    $model = $sanpham[0]['model'];
    $price = $sanpham[0]['price'];
    $year = $sanpham[0]['year'];
    $img = $sanpham[0]['img'];
}
else
?>