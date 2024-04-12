<?php
    if (isset($_POST['delete']))
    {
        $delete = $_POST['delete'];
        $obj->delete($delete);
    }
    if (isset($_POST["update"]))
    {
        $_SESSION['id_car_update']= $_POST['update'];
        header('Location: index.php?page=update');
    }
?>