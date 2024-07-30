<?php
    $conn = mysqli_connect("localhost", "root", "", "e_inventories");

    // koneksi check
    if (mysqli_connect_errno()) {
        echo "Koneksi database gagal : " . mysqli_connect_error();
    }