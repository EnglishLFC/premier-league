# Premier League Widget for Ubersicht
#
# Copyright: Nigel Houghton <wutang@warpten.net>
#
# Execute the shell command.
command: "premier-league.widget/premier-league.py"

# Set the refresh frequency (milliseconds).
refreshFrequency: 1000000

# Render the output.
render: (output) -> """
<div class="BigTable">#{output}</div>
"""

# CSS Style
style: """
  xxwidth:140px
  top: 6pt
  right: 6pt
  font-family: Hack, Myriad Set Pro, Helvetica Neue
  background:rgba(#000, 0.0)
  border: none
  border-radius:10px
  text-align:center
  font-size:10pt

  .Wrapper, .LastWrapper
    xxwidth:100%
    display:inline-block

  .BigTable
    padding:6px
    padding-bottom:0px

// Change the RGB values here for a different color
  .mightiest
    color: #f00
    vertical-align: middle
    text-align: center

// Change the RGB values here for a different color
  .themighty
    color: #f00
    vertical-align: middle
    text-align: left

  .numbers
    vertical-align: middle
    text-align: center

  table
    border-collapse: collapse
    border: 1px solid
    border-color: rgba(255,255,255,0.50)

  tr,th,td
    border-collapse: collapse
    border: 1px solid
    border-color: rgba(255,255,255,0.50)
    text-align: left
    vertical-align: middle
    padding: 5px
    color: rgba(255,255,255,0.50)

"""
