	print qq~
</td>
</tr>
</table>
</td>
</tr>
</table>
</td>
</tr>
</table>
</td>

<!--

<td valign="top" width="150">
<table width="150">
<tr>
<td>

-->

<tr>
<td>
~;
	

	print qq~</td>
</tr>
<tr>
<td>

~;

	print qq~</td>
</tr>
</table>
</td>
</tr>
</table>
</div>
~;

mycontent_block2(); 

print qq~

<div align="center">
<table class="pagetable">
    <tr> 
      <td height="21">~;
menu_bar();
      print qq~</td>
    </tr>
    <tr> 
     <td>~;
about_bar();
print qq~</div>
<div align="center">~;

print qq~</div>

</html>
~;


1; # return true

