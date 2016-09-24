QUnit.test( "errors should be hidden on keypress", function(assert) {
  $('input').trigger('keypress');
  assert.equal($('.has-error').is(':visible'), true);
});

QUnit.test( "errors should not be hidden unless there is a keypress", function(assert) {
  assert.equal($('.has-error').is(':visible'), true);
});