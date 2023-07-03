from string import Template


INDEX_TEMPLATE = Template("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Wizard API Docs</title>
    <link rel="shortcut icon" href="assets/favicon.ico">
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
          integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <!-- Custom CSS -->
    <link rel="stylesheet" href="assets/style.css">
    <!-- Custom JS -->
    <script src="assets/custom.js"></script>
</head>
<body>

<header>
    <h1>
        <img src="./assets/logo.svg" alt="Logo" class="logo">
        <div class="title">| API Docs</div>
    </h1>
</header>

<div class="article">
    <h2>API Spec</h2>
    
    <table class="table table-striped">
        <thead>
        <tr>
            <th scope="col">Version</th>
            <th scope="col" colspan="2">Link</th>
        </tr>
        </thead>
        <tbody>
            $apiDocsRows
        </tbody>
    </table>
    
    <h2>Changes</h2>
    
    <table class="table table-striped">
        <thead>
        <tr>
            <th scope="col">From</th>
            <th scope="col">To</th>
            <th scope="col">Link</th>
        </tr>
        </thead>
        <tbody>
            $changesRows
        </tbody>
    </table>
</article>

<!-- Bootstrap JS -->
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
        integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
        crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
        integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1"
        crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
        integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM"
        crossorigin="anonymous"></script>
</body>
</html>
""")
