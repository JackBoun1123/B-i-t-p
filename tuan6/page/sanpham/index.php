<?php
$list = 8;
$page = isset($_GET['pg']) ? $_GET['pg'] : 1;
$offset = ($page - 1) * $list;
$obj = new database();
if($cate)
    $sql="select * from supercars where brand='$cate' LIMIT $list OFFSET $offset";
else
    $sql="select * from supercars LIMIT $list OFFSET $offset";
$sanpham=$obj->xuatdulieu($sql);
if($sanpham)
{
    for($i=0;$i<count($sanpham);$i++) 
    {
        echo    '<a href="index.php?page=detail&item='.$sanpham[$i]['car_id'].'">';
        echo '<div class="sanpham">
                
                <div class="tensp">'.$sanpham[$i]["model"].'</div>
                <div class="hinh"><img src="upload/sanpham/'.$sanpham[$i]["img"].'" width=300px; height=205px;" /></div>
                <div class="gia">Giá: '.number_format($sanpham[$i]["price"]).'$</div>
            </div>';
        echo    "</a>";
    }
}
else
    echo "<script>alert('Hiện chưa có sản phẩm')</script>";
if ($cate)
    $sql="select * from supercars where brand='$cate'";
else
    $sql="select * from supercars";
$sanpham=$obj->xuatdulieu($sql);
echo    "<div class='pg'>";
for($i=0;$i<(count($sanpham)/$list);$i++) 
{
    echo '<a href="index.php?page=sanpham&cate='.$cate.'&pg='.($i+1).'"><button style="margin:10px; width:40px;"  name="pg" value='.$i.'>'.($i+1).'</button></a>';
}
echo    "</div>";
?>
<div style="clear:both"></div>

    
