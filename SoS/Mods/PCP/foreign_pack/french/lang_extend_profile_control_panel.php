<?php
/***************************************************************************
 *						lang_extend_profile_control_panel.php [French]
 *						-------------------------------------
 *	begin				: 28/09/2003
 *	copyright			: Ptirhiik
 *	email				: ptirhiik@clanmckeen.com
 *
 *	version				: 1.0.0 - 30/09/2003
 *
 * Profile Control Panel v 1.0.2
 *
 ***************************************************************************/

/***************************************************************************
 *
 *   This program is free software; you can redistribute it and/or modify
 *   it under the terms of the GNU General Public License as published by
 *   the Free Software Foundation; either version 2 of the License, or
 *   (at your option) any later version.
 *
 ***************************************************************************/

if ( !defined('IN_PHPBB') )
{
	die("Hacking attempt");
}

// admin part
if ( $lang_extend_admin )
{
	$lang['Lang_extend_profile_control_panel'] = 'Profile Control Panel';
}

// who's online
$lang['Admin_founder_online_color']			= '%sFondateur%s';
$lang['User_online_color']					= '%sUtilisateur%s';

// topic or privmsg display
$lang['Add_to_friend_list']					= 'Ajouter à votre liste d\'amis';
$lang['Remove_from_friend_list']			= 'Retirer de votre liste d\'amis';
$lang['Add_to_ignore_list']					= 'Ajouter à votre liste d\'ignorés';
$lang['Remove_from_ignore_list']			= 'Retirer de votre liste d\'ignorés';
$lang['Happy_birthday']						= 'Joyeux Anniversaire !';
$lang['Ignore_choosed']						= 'Vous avez choisi d\'ignorer cet utilisateur';
$lang['Online']								= 'En ligne';
$lang['Offline']							= 'Hors ligne';
$lang['Hidden']								= 'Caché';
$lang['Gender']								= 'Sexe';
$lang['Male']								= 'Masculin';
$lang['Female']								= 'Féminin';
$lang['No_gender_specify']					= 'Non Spécifié';
$lang['Age']								= 'Age';
$lang['Do_not_allow_pm']					= 'Cet utilisateur n\'accepte pas les messages privés';

// main entry (profile.php)
$lang['Click_return_profilcp']				= 'Cliquez %sici%s pour retourner à la maintenance du profil.';

// birthday popup (profile_birthday.php)
$lang['Birthday']							= 'Anniversaire';
$lang['birthday_msg']						= 'Bonjour %s, <br /><br /><br /> %s est heureux de vous souhaiter un Joyeux Anniversaire !';

// home panel (profilcp_home.php)
$lang['profilcp_index_shortcut']			= 'Accueil';
$lang['profilcp_index_pagetitle']			= 'Accueil du panneau de contrôle du profil';

// home panel : mini buddy list (functions_profile.php)
$lang['Friend_list']						= 'Liste d\'amis';
$lang['Friend_list_of']						= 'Ami de';
$lang['Ignore_list']						= 'Liste d\'ignorés';
$lang['Ignore_list_of']						= 'Ignoré par';
$lang['Nobody']								= 'Personne';
$lang['Always_visible']						= 'Toujours visible pour cet utilisateur';
$lang['Not_always_visible']					= 'Cet utilisateur ne vous verra pas lorsque vous serez en mode caché';

// home panel : watched topics (functions_profile.php)
$lang['Stop_watching_selected_topics']		= 'Se désabonner des sujets sélectionnés';
$lang['New_subscribed_topic']				= 'Sujets abonnés';
$lang['Submit_period']						= 'Voir les sujets datant de';

// buddy list (profilcp_buddy.php)
$lang['profilcp_buddy_shortcut']			= 'Listes de membres';
$lang['profilcp_buddy_pagetitle']			= 'Listes de membres';
$lang['profilcp_buddy_friend_shortcut']		= 'Liste d\'amis';
$lang['profilcp_buddy_friend_pagetitle']	= 'Editer votre liste d\'amis';
$lang['profilcp_buddy_ignore_shortcut']		= 'Liste d\'ignorés';
$lang['profilcp_buddy_ignore_pagetitle']	= 'Editez votre liste d\'ignorés';
$lang['profilcp_buddy_list_shortcut']		= 'Tous les membres';
$lang['profilcp_buddy_list_pagetitle']		= 'Liste de tous les membres';
$lang['Click_return_privmsg']				= 'Cliquez %sici%s pour retourner aux messages privés.';
$lang['profilcp_buddy_could_not_add_user']	= 'L\'utilisateur que vous avez choisi n\'existe pas.';
$lang['profilcp_buddy_could_not_anon_user']	= 'Vous ne pouvez pas enregistrer l\'Invité dans une de vos listes de membres.';
$lang['profilcp_buddy_add_yourself']		= 'Vous ne pouvez pas vous enregistrer dans une de vos listes';
$lang['profilcp_buddy_already']				= 'Cet utilisateur est déjà dans une de vos listes';
$lang['profilcp_buddy_ignore']				= 'Ajout impossible : cet utilisateur vous ignore';
$lang['profilcp_buddy_you_admin']			= 'Puisque vous êtes un administrateur ou un modérateur, vous ne pouvez ignorer les membres du forum';
$lang['profilcp_buddy_admin']				= 'Vous ne pouvez pas placer en liste d\'ignorés un administrateur ou un modérateur';
$lang['User_fields']						= 'Liste des zones utilisateur';
$lang['Friend']								= 'Amis';
$lang['Comp_LE']							= 'est inférieur à';
$lang['Comp_EQ']							= 'est égal à';
$lang['Comp_NE']							= 'est différent de';
$lang['Comp_GE']							= 'est plus grand que';
$lang['Comp_IN']							= 'contient';
$lang['Comp_NI']							= 'ne contient pas';
$lang['Sort_none']							= 'Non trié';
$lang['date_entry']							= 'AAAAMMJJ';

// update profile (profilcp_profil.php)
$lang['profilcp_profil_shortcut']			= 'Profil';
$lang['profilcp_profil_pagetitle']			= 'Edition du profil';
$lang['profilcp_prefer_shortcut']			= 'Votre profil';
$lang['profilcp_prefer_pagetitle']			= 'Vos préferences pour votre profil';
$lang['profilcp_signature_shortcut']		= 'Signature';
$lang['profilcp_signature_pagetitle']		= 'Signature';
$lang['profilcp_avatar_shortcut']			= 'Avatar';
$lang['profilcp_avatar_pagetitle']			= 'Avatar';

// update profile : preferences - functions (mod_profile_control_panel.php)
$lang['Other']								= 'Autre...';
$lang['Friend_only']						= 'Seulement pour mes amis';

// update profile : public informations : web info (mod_profile_control_public_web.php)
$lang['profilcp_profil_base_shortcut']		= 'Informations publiques';
$lang['Web_info']							= 'Informations du web';

// update profile : public informations : real info (mod_profile_control_public_real.php)
$lang['Real_info']							= 'Informations personnelles';
$lang['Realname']							= 'Nom réel';
$lang['Date_error']							= '%d/%d/%d n\'est pas une date valide.';

// update profile : public informations : messengers info (mod_profile_control_public_messengers.php)
$lang['Messangers']							= 'Les messagers';

// update profile : public informations : contact info (mod_profile_control_public_contact.php)
$lang['Home_phone']							= 'N° de téléphone du domicile';
$lang['Home_fax']							= 'N° de fax du domicile';
$lang['Work_phone']							= 'N° de téléphone du travail';
$lang['Work_fax']							= 'N° de fax du travail';
$lang['Cellular']							= 'N° de portable';
$lang['Pager']								= 'N° de pager';

// update profile : preferences - home panel (mod_profile_control_panel_home.php)
$lang['Profile_control_panel']				= 'Réglages du profil';

// update profile : preferences - i18n panel (mod_profile_control_panel_international.php)
$lang['Profile_control_panel_i18n']			= 'Internationalisation';
$lang['summer_time']						= 'Etes-vous dans un pays qui pratique le changement d\'heure été/hiver ?';

// update profile : preferences - notification panel (mod_profile_control_panel_notification.php)
$lang['Profile_control_panel_notification']	= 'Notification';

// update profile : preferences - posting panel (mod_profile_control_panel_posting.php)
$lang['Profile_control_panel_posting']		= 'Postage';

// update profile : preferences - privacy panel (mod_profile_control_panel_privacy.php)
$lang['Profile_control_panel_privacy']		= 'Privé';
$lang['View_user']							= 'Me montrer "En ligne"';
$lang['Public_view_pm']						= 'Accepter les messages privés';
$lang['Public_view_website']				= 'Afficher mes informations internet';
$lang['Public_view_messengers']				= 'Afficher mes références de messagers';
$lang['Public_view_real_info']				= 'Afficher mes informations personnelles';

// update profile : preferences - reading panel (mod_profile_control_panel_reading.php)
$lang['Profile_control_panel_reading']		= 'Lecture';
$lang['Public_view_avatar']					= 'Voir les avatars';
$lang['Public_view_sig']					= 'Voir les signatures';
$lang['Public_view_img']					= 'Voir les images';

// update profile : preferences - profile preferences
$lang['profile_prefer']						= 'Options du profil';

// update profile : preferences - system panel (mod_profile_control_panel_system.php)
$lang['Profile_control_panel_system']		= 'Système';
$lang['summer_time_set']					= 'Est-ce l\'heure d\'été ? (ajout de +1 heure à l\'heure locale)';
$lang['Forum_rules']						= 'N° de sujet contenant la charte du forum';

// update profile : preferences - admin part (mod_profile_control_panel_admin.php)
$lang['profilcp_admin_shortcut']			= 'Admin';
$lang['User_deleted']						= 'L\'utilisateur a été supprimé avec succès.';
$lang['User_special']						= 'Champs spéciaux pour administrateurs uniquement';
$lang['User_special_explain']				= 'Ces champs ne peuvent pas être modifées par l\'utilisateur. Ici, vous pouvez définir leur statut et d\'autres options non données aux utilisateurs.';
$lang['User_status']						= 'L\'utilisateur est actif';
$lang['User_allow_email']					= 'Peut envoyer des emails';
$lang['User_allow_pm']						= 'Peut envoyer des Messages Privés';
$lang['User_allow_website']					= 'Peut publier ses informations internet';
$lang['User_allow_messanger']				= 'Peut publier ses adresses de messangers';
$lang['User_allow_real']					= 'Peut publier ses informations personnelles';
$lang['User_allowavatar']					= 'Peut afficher un avatar';
$lang['User_allow_sig']						= 'Peut afficher sa signature';
$lang['Rank_title']							= 'Titre du Rang';
$lang['User_delete']						= 'Supprimer cet utilisateur';
$lang['User_delete_explain']				= 'Cochez cette case pour supprimer cet utilisateur ; ceci ne peut pas être rétabli.';
$lang['No_assigned_rank']					= 'Aucun rang spécial assigné';
$lang['User_self_delete']					= 'Vous ne pouvez pas supprimer votre profil, étant un adminsitrateur.';

// update profile : signature (profilcp_profile_signature.php)
$lang['profilcp_sig_preview']				= 'Aperçu de la signature';

// display profile (profilcp_public.php)
$lang['profilcp_public_shortcut']			= 'Public';
$lang['profilcp_public_pagetitle']			= 'Partie publique';
$lang['profilcp_public_base_shortcut']		= 'Fiche';
$lang['profilcp_public_base_pagetitle']		= 'Informations de base du profil';
$lang['profilcp_public_groups_shortcut']	= 'Groupes';
$lang['profilcp_public_groups_pagetitle']	= 'Les groupes auquels appartient cet utilisateur';

// update profile : preferences - home panel (mod_profile_control_panel_home.php)
$lang['Profile_control_panel_home']			= 'Accueil';
$lang['Profile_control_panel_home_buddy']	= 'Liste de membres';
$lang['Buddy_friend_display']				= 'Afficher ma liste d\'amis sur l\'accueil';
$lang['Buddy_ignore_display']				= 'Afficher ma liste d\'ignorés sur l\'accueil';
$lang['Buddy_friend_of_display']			= 'Afficher la liste "Ami de" sur l\'accueil';
$lang['Buddy_ignored_by_display']			= 'Afficher la liste "Ignoré par" sur l\'accueil';

$lang['Profile_control_panel_home_privmsg']	= 'Messages privés';
$lang['Privmsgs_per_page']					= 'Nombre de messages privés affichés par page sur l\'accueil';

$lang['Profile_control_panel_home_wtopics']	= 'Sujets abonnés';
$lang['Watched_topics_per_page']			= 'Nombre de sujets abonnés par page sur l\'accueil';

// display profile : base info (profilcp_public_base.php)
$lang['Unavailable']						= 'Non disponible';
$lang['Last_visit']							= 'Dernière visite';
$lang['User_posts']							= 'Message de l\'utilisateur';
$lang['User_post_stats']					= '%s messages, %.2f%% du total, %.2f messages par jour';
$lang['Most_active_topic']					= 'Sujet de prédilection';
$lang['Most_active_topic_stat']				= '%s messages, %.2f%% du sujet, %.2f%% du forum';
$lang['Most_active_forum']					= 'Forum de prédilection';
$lang['Most_active_forum_stat']				= '%s messages, %.2f%% du forum, %.2f%% du total';

// register (profilcp_register.php)
$lang['profilcp_register_shortcut']			= 'Enregistrement';
$lang['profilcp_register_pagetitle']		= 'Informations d\'enregistrement';
$lang['profilcp_email_title']				= 'Adresse Email';
$lang['profilcp_email_confirm']				= 'Confirmez votre adresse Email';
$lang['anti_robotic']						= 'Image de contrôle';
$lang['anti_robotic_explain']				= 'Ce contrôle est là pour éviter les robots d\'enregistrement automatique';
$lang['profilcp_password_explain']			= 'Vous devez saisir votre mot de passe actuel si vous voulez le changer';
$lang['Agree_rules']						= 'En cochant cette case, vous déclarez avoir pris connaissance des termes de la charte de ces forums, et être en accord avec ceux-ci.';
$lang['profilcp_username_missing']			= 'Le nom du profil manque';
$lang['profilcp_email_not_matching']		= 'Les adresses Email ne correspondent pas';
$lang['Robot_flood_control']				= 'L\'image de contrôle ne correspond pas à votre saisie';
$lang['Disagree_rules']						= 'Vous avez déclarez ne pas être en accord avec la charte de ces forums ; vous ne pouvez donc pas vous enregistrer.';

?>