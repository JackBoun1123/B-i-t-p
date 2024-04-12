<?php
class database
{
    private function connect()
    {
        $conn = new mysqli("127.0.0.1","root","","db_bennis_store");
        $conn->set_charset("utf8");
        if ($conn -> connect_errno)
        {
            echo "ket noi KHONG thong cong";
            exit();
        }
        else
            return $conn;
    }
    public function xuatdulieu($sql)
    {
        $arr = array();
        $link=$this->connect();
        $result=$link->query($sql);
        if($result->num_rows)
        {
            while($row=$result->fetch_assoc())
                $arr[]=$row;
            return $arr;
        }
        else
            return 0;
    }
    public function thucthi($sql)
    {
        $link = $this -> connect();
        if ($link-> query($sql))
        {
            return 1;
        }
        else 
            return 0;
    }
    
}
?>