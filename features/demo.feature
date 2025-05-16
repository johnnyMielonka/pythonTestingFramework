Feature: Behave FW basic functionality
  Background:
    Given Start new "chrome" browser

    Scenario: Demo test for AuroraCommerce
      Given Open "https://demo.auroracommerce.com" url
      When Click on menu item
        |item|
        |Sale|
        |Shoes|
        |Jewellery|
        |Accessories|
        |Clothes|
        |Demo Category|
        |New In|
      Then Verify if following menu bar items are available
        |item|
        |SALE|
        |SHOES|
        |JEWELLERY|
        |ACCESSORIES|
        |CLOTHES|
        |DEMO CATEGORY|
        |NEW IN|


  Scenario Outline: Run a simple test on <url> web page
    Given Open "<url>" url
    When Go to login page
    And log in as "test" user and "aaaa" password
    Then Verify if page title is <title>

    Examples: bsstack
      | url                      | title     |
      | https://bstackdemo.com/  | StackDemo |

  Scenario Outline: Another simple test on <url> web page
    Given Open "<url>" url
    Then Verify if page title is <title>

    Examples: WebPages
      | url                 | title                                                         |
      | https://pepper.pl/  | Pepper.pl - Najlepsze Okazje, Rabaty, Promocje i Błędy Cenowe |
      | https://allegro.pl/ | allegro.pl                                                    |

