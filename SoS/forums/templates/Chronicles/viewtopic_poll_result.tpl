 
<tr> 
  <td class="row2" colspan="2"><br clear="all" />
	<table cellspacing="0" cellpadding="4" border="0" align="center">
	  <tr> 
		<td colspan="4" align="center"><span class="gentbl"><b>{POLL_QUESTION}</b></span></td>
	  </tr>
	  <tr> 
		<td align="center"> 
		  <table cellspacing="0" cellpadding="2" border="0">
			<!-- BEGIN poll_option -->
			<tr> 
			  <td><span class="gentbl">{poll_option.POLL_OPTION_CAPTION}</span></td>
			  <td> 
				<table cellspacing="0" cellpadding="0" border="0">
				  <tr> 
					<td><img src="templates/Chronicles/images/vote_lcap.gif" width="6" alt="" height="12" /></td>
					<td><img src="{poll_option.POLL_OPTION_IMG}" width="{poll_option.POLL_OPTION_IMG_WIDTH}" height="12" alt="{poll_option.POLL_OPTION_PERCENT}" /></td>
					<td><img src="templates/Chronicles/images/vote_rcap.gif" width="6" alt="" height="12" /></td>
				  </tr>
				</table>
			  </td>
			  <td align="center"><b><span class="gentbl">&nbsp;{poll_option.POLL_OPTION_PERCENT}&nbsp;</span></b></td>
			  <td align="center"><span class="gentbl">[ {poll_option.POLL_OPTION_RESULT} ]</span></td>
			</tr>
			<!-- END poll_option -->
		  </table>
		</td>
	  </tr>
	  <tr> 
		<td colspan="4" align="center"><span class="gentbl"><b>{L_TOTAL_VOTES} : {TOTAL_VOTES}</b></span></td>
	  </tr>
	</table>
	<br clear="all" />
  </td>
</tr>
