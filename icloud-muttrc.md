---
title: icloud-muttrc
date-created: 2018-03-23T22:26
tags: wiki,mutt,icloud
---

## icloud-muttrc

***

```bash
set folder = "~/Mail"
source ~/.mutt/mailboxes

set spoolfile = "+icloud/INBOX"
set record = "+icloud/Sent\ Messages"
set postponed = "+icloud/Drafts"
set trash = "+icloud/Deleted\ Messages"
set editor = nvim

source "gpg -dq ~/.mutt/realname.gpg |"
source "gpg -dq ~/.mutt/from.gpg |"

set realname = $my_realname
set from = $my_from
set sendmail = "/usr/bin/sendmail"
set edit_headers = yes

set text_flowed = yes

source mutt-colors-solarized-dark-16.muttrc
```

### vim filetype

```viml
#vim:ft=muttrc

folder-hook 'user.mail.school.edu'		'source ~/.config/mutt/accounts/school-gmail'
folder-hook 'user1.gmail.com'			'source ~/.config/mutt/accounts/gmail1'
folder-hook 'user2.gmail.com'			'source ~/.config/mutt/accounts/gmail2'
folder-hook 'user.icloud.com'			'source ~/.config/mutt/accounts/icloud'
folder-hook 'user.rocketmail.com'		'source ~/.config/mutt/accounts/yahoo'
folder-hook 'user.aol.com'			'source ~/.config/mutt/accounts/aol'
```

```bash
#---------------------------------------------------------------
## file:     ~/.mutt/iCloud.muttrc
## iCloud specific options
## author:   Alexander Strassheim
## vim:fenc=utf-8:nu:ai:si:et:ts=4:sw=4:ft=sh
#---------------------------------------------------------------

# Settings
set from          = $my_from_personal
set folder        = imaps://imap.mail.me.com:993/
set spoolfile     = +Inbox
set postponed     = +Drafts
set record        = "+Sent Messages"
set trash         = "+Deleted Messages"

# Receive options
set imap_user     = $my_imap_personal
set imap_pass     = $my_pw_personal

# Send options
set smtp_url      = smtp://$imap_user@smtp.mail.me.com:587/
set smtp_pass     = $my_pw_personal
set imap_check_subscribed

# macro index S "<save-message>+iCloud/INBOX.Spam<enter>"   "mark message as spam"
```

```bash
source ~/.mutt/config/muttrc_icloud

# editor settings
set editor = 'vim + -c "set textwidth=72" -c "set wrap" -c "set nocp" -c "setlocal spell! spelllang=en_us,bg" -c "nnoremap <F2> :wq<CR>"'

# caching
set header_cache = ~/.mutt/cache/headers
set message_cachedir = ~/.mutt/cache/bodies
set certificate_file = ~/.mutt/certificates

# aliases
source ~/.mutt/config/muttrc_bindings_generic

set index_format="%4C %Z %{%b %d} %-15.15n %?M? (%4l)? %?y?{%.20Y} ?%s"
set status_format="%f (%u/%m) %> %P"

# sorting
set sort = threads
set sort_aux = reverse-date-received

# number of messages to display when pager is visible
set pager_index_lines = 10

set postpone = ask-no                     # Ask about postponing.
set include                               # Include the message in replies.
set attribution = "On %{%a, %e %B %Y at %R }, %n wrote:"   # Format of replies
set edit_headers                          # I want to edit the message headers.
set copy                                  # Keep copies of outgoing mail...
set fcc_clear                             # Keep fcc's clear of signatues and encryption.
set tilde                                 # Fill out messages with '~'.
set noconfirmappend                       # Just append, don't hassle me.
set pager_stop                            # Don't skip msgs on next page.
set fast_reply                            # do not ask about To: and Subject when replying
unset mark_old                            # do not mark messages as old

# don't ask for purge
set delete = yes

# colors
source ~/.mutt/config/muttrc_colors

auto_view text/html

# headers
ignore *
unignore From: To: CC: Subject: Date:
unhdr_order *
hdr_order From: To: Date: CC: Subject:
```



## References


[muttrc](https://github.com/rahulsalvi/dotfiles/blob/9b727496769c4ca9126fe61bea14b983d948a6dc/mutt/muttrc)

***

[[Home]]()
