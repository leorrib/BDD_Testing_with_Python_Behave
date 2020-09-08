Feature: Carrinho de Compras
	I would like search for an item
	Pick a color if item exists
	Validate shop cart

	@positive
	Scenario Outline: Validating shop-cart
		Given the user searches for "<item>" at the homepage
		When picks the color "<desired_color>" for the "<item>" and adds the item to the cart
		Then verifies that "<amount>" item "<item>", with price "<price>" and color "<desired_color>", was added to the cart and checks the final price

		Examples:
			| item     | amount | price   | desired_color |
			| T-SHIRT  | 1      | $16.51  | blue          |
			| BLOUSE   | 1      | $27.00  | white 	      |

	@negative
	Scenario: Product not found
		Given the user searches for "dummy item" at the homepage
		Then verifies that the item is not available and that the message "No results were found for your search "dummy item"" is displayed