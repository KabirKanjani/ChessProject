<?php
$target_dir = "./PNGs/";
$target_dir = $target_dir . basename( $_FILES["image"]["name"]);
$uploadOk=1;

if (move_uploaded_file($_FILES["image"]["tmp_name"], $target_dir)) {
    echo "The file ". basename( $_FILES["image"]["name"]). " has been uploaded.";
} else {
    echo "Sorry, there was an error uploading your file.";
  }
?>