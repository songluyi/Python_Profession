<html xmlns=http://www.w3.org/1999/xhtml>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>有效代理IP获取轮子</title>
<!--    下面开始引入bootstrap内容-->
    <!-- 新 Bootstrap 核心 CSS 文件 -->
    <link rel="stylesheet" href="styles/bootstrap.min.css">

    <!-- 可选的Bootstrap主题文件（一般不用引入） -->
    <link rel="stylesheet" href="styles/bootstrap-theme.min.css">

    <!-- jQuery文件。务必在bootstrap.min.js 之前引入 -->
    <script src="scripts/jquery.min.js"></script>

    <!-- 最新的 Bootstrap 核心 JavaScript 文件 -->
    <script src="scripts/bootstrap.min.js"></script>
</head>
<body>
<div class="col-md-12 column">
    <h1 class="text-center">这就是一个简单代理轮子</h1>
</div>
<?php
echo "<table class=\"table table-bordered\"style='border: solid 1px black;'>";
echo "<tr><th>IP</th><th>PORT</th><th>HIDE</th><th>CONNECTONS</th><th>WAY</th><th>PLACE</th><th>PING</th><th>LIVE</th></tr>";

class TableRows extends RecursiveIteratorIterator {
    function __construct($it) {
        parent::__construct($it, self::LEAVES_ONLY);
    }

    function current() {
        return "<td style='width: 150px; border: 1px solid black;'>" . parent::current(). "</td>";
    }

    function beginChildren() {
        echo "<tr>";
    }

    function endChildren() {
        echo "</tr>" . "\n";
    }
}

$servername = "123.206.203.57:3306";
$username = "root";
$password = "070801382";
$dbname = "world";

try {
    $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $stmt = $conn->prepare("SELECT * FROM proxy_db");
    $stmt->execute();

    // 设置结果集为关联数组
    $result = $stmt->setFetchMode(PDO::FETCH_ASSOC);

    foreach(new TableRows(new RecursiveArrayIterator($stmt->fetchAll())) as $k=>$v) {
        echo $v;
    }
    $dsn = null;
}
catch(PDOException $e)
{
    echo "Error: " . $e->getMessage();
}
$conn = null;
echo "</table>";
?>
</body>
