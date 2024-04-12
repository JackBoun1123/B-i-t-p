<?php
    class congty extends database
    {
        public function danhsachsanpham($id ='')
        {
            if ($id)
                $sql = "Select * from supercars where car_id= '$id'";
            else
                $sql= 'Select * from supercars';
            return $this->xuatdulieu($sql);
        }
        public function delete($id='')
        {
            $sql ="Delete from supercars where car_id='$id'";
            return $this->thucthi($sql);
        }
        public function themtaikhoan($name, $hometown, $email, $phone, $pass)
        {
            $sql= "
                Insert into employees (full_name, home_town, email, phone_number, password)
                values ('$name', '$hometown', '$email', '$phone', '$pass');
            ";
            return $this->thucthi($sql);
        }
        public function kiemtradangnhap($email, $pass)
        {
            $pass = md5($pass);
            $sql = "SELECT employee_id FROM employees WHERE email='$email' AND password='$pass'";
            $result = $this->xuatdulieu($sql);
            if ($result != 0) {
                return $result[0]["employee_id"];
            } else {
                return 0;
            }
        }
        public function tentaikhoan($id)
        {
            $sql= "select full_name from employees where employee_id='$id'";
            $result = $this->xuatdulieu($sql);
            if ($result != 0) {
                return $result[0]["full_name"];
            } else {
                return 0;
            }
        }
        
        
    }
?>