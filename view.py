


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>
   dashboard
</title>
    <link href="/static/css/base.css" rel="stylesheet">
</head>

<body>
<div id="header" style="background-color: #666666;">
 <span class="logo"><a href="/" style="color: #ffefef;">E-Com Trial</a></span>
    <div class="search-bar mt-sm-2 mr-2 text-center" style="max-width: 500px; width: 100%;">

 
            <!-- search box-->

      <form method="GET" class="navbar-form navbar-right" role="search" action="/search/" required>
        <div class="form-group ">
          <input type="text" class="form-control" placeholder="Product Search" value="" name="q">
            <button type="submit" class="btn btn-primary"><span class="glyphicon glyphicon-search"></span>Search</button>
        </div>

      </form>
 


    </div>
    <div class="text-right">
        
        <a href="/accounts/login/">Login</a>
        <a href="/accounts/register/">Signup</a>
        
    </div>
</div>
<div id="subheader">

    <div class="cart">
        
            
                Your cart is Empty.
            
        
    </div>
</div>
<div id="content">
    
    <div class="row">
    
    </div>
    <div id="sidebar">
    <h3>Categories</h3>
    <ul>
        <li  class="selected">
        <a href="/">All</a>
        </li>
    
        <li >
        <a href="/kfc/">KFC</a>
        </li>
    
        <li >
        <a href="/pizza/">Pizza</a>
        </li>
    
    </ul>
    </div>
    <div id="main" class="product-list">
    <h1>Products</h1>
    
        <div class="item" style="margin: 5px;">
            <a href="/2/large-pizza/"><img src="/media/products/22/12/17/pizzaa.png" alt="" width="275" height="275" style="border-radius: 5px;"></a>
            <a href="/2/large-pizza/">Large-Pizza</a>
            <br>
            $10.00
        </div>
    
        <div class="item" style="margin: 5px;">
            <a href="/3/small-pizza/"><img src="/media/products/22/12/17/pizza_AUPC7R1.png" alt="" width="275" height="275" style="border-radius: 5px;"></a>
            <a href="/3/small-pizza/">small-pizza</a>
            <br>
            $45.00
        </div>
    
        <div class="item" style="margin: 5px;">
            <a href="/4/wing/"><img src="/media/products/22/12/17/kfc.png" alt="" width="275" height="275" style="border-radius: 5px;"></a>
            <a href="/4/wing/">wing</a>
            <br>
            $10.00
        </div>
    
    </div>

</div>
</body>
</html>
