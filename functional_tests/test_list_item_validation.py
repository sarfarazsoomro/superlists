from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):

  def test_cannot_add_empty_list_itemss(self):
    # Edith goes to the home page and accidentally tries to input and empty list item/
    # She hits enter on the empty input box

    # The home page refreshes and there's an error message saying that the list items
    # cannot be blank

    # She tries again with some text for the item. Which now works

    # Perversely she now decides to input second blank item

    # She receives a similar warning on the lists page

    # And she can correct it by filling some text in
    self.fail('Write me!')
