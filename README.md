#Welcome to E Commerce website Testing

#Set Up The FrameWork:

# 1.Important things:

• The project supports only chrome.

• The project supports only WordPress sites.

• You must install WooCommerce in your WordPress through the plugins.

• Check your browser version for the web driver. (Version 107 included in the 
project)

• If your using Local to run WordPress locally you will need to fill the port option.

•tcids3  "test_register_new_user_failed()" will fail you need to set it up manually with existing user.

•Instructions on how to run on DOcker and Jenkins will be added soon.
•PDF file provided whoever dislikes MD files.




# Must do in WordPress :

1) Download the zip file file from here if u run WordPress locally.

2) Pull the sample_products.xml from the zip then Go back to WordPress: Tools -> 
WordPress -> install -> run Importer -> choose file -> provide the location of the XML 
file.

3) Settings -> reading -> click on A static page ->change homepage to shop

4) Settings -> general -> check Anyone can register.

5) WooCommerce -> settings -> Accounts & Privacy -> “Guest checkout” check all, 
“Account Creation” check all but the last one. 

6) Must create coupon code: marketing -> coupon (coupon type percentage discount)


# 2.set up the Credantials.ps1:

• WC_KEY – WordPress public key

• WC_SECRET – WordPress secret key

 *NOTE: im using MYSQL.

• DB_USER – Database Login Name (default root)

• DB_PASSWORD - Database Password (default root)

• DB_SERVER – Database Host(default localhost, if you’re using VMware for DB 
you will need to provide the IP of the iso.)

• DB_NAME – Database Table Name. (same DB as you’re WordPress site)


• SELPATH – Selenium Driver Path. (click here or you can set up manually)

• ENVSEL – The URL of the site.

• COUPON – the name of your coupon.

• PORT - the port you’re using to run WordPress Database. (optional – for local 
users)

• Host - machine = ur local pc , docker= docker container


# 3.Set up The Testing Environment:

1) Create python virtual environment:

1.1) pip install virtualenv

1.2) py -m venv {Name for your virtual environment.}

1.3) open IDE make the virtual environment as main virtual environment.

*)PyCharm – file -> settings -> Project -> python interpreter -> -> add -> new 
environment -> click on Location -> paste you’re python.exe path

1.4) activate your virtual environment.

1.5) install/develop setup.py, command: python setup.py install.



# 4. Set Up The Selenium Path:

1) copy the chrome driver.exe to the “front” folder.

1.1) execute the getpath.py.

1.2) copy the path you got in the terminal to Credantials.ps1 (SELPATH=” whatever path 
you have copied”).

# 5.Testing Section:

BackEnd Section:

• tcid stands for – test case id.

• tcidc stands for – test case id for customers.

• tcidp stands for – test case id for products.

• tcido stands for – test case id for orders.

• customers – pytest -m customers. (Run all the costumer tests)

• products – pytest -m products. (Run all the product tests.)

• orders – pytest -m orders. (Run all the orders tests)

Selenium Section:

• tcids stands for – test case id for selenium.

Run all tests - pytest


*) check the PDF file for every test and for its id.


• if you would like to add more tests here the docs.
• https://woocommerce.github.io/woocommerce-rest-apidocs/#introduction
