Feature: Behave FW basic functionality

   Scenario Outline: Run a simple test on <url> web page
    Given Open <url> url
    When Go to login page
    And log in as "test" user and "aaaa" password
    Then Verify if page title is <title>

    Examples: bsstack
      | url                      | title     |
      | https://bstackdemo.com/  | StackDemo |

  Scenario Outline: Another simple test on <url> web page
    Given Open <url> url
    Then Verify if page title is <title>

    Examples: WebPages
      | url                 | title                                                         |
      | https://pepper.pl/  | Pepper.pl - Najlepsze Okazje, Rabaty, Promocje i Błędy Cenowe |
      | https://allegro.pl/ | allegro.pl                                                    |