from blockchain import blockexplorer
tx = blockexplorer.get_tx('8bae12b5f4c088d940733dcd1455efc6a3a69cf9340e17a981286d3778615684')
tx.outputs[0].script # gives unicode string, u'6a13636861726c6579206c6f766573206865696469'
print tx.outputs[0].script
