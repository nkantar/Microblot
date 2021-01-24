# Microblot

Microblot is a chat bot for microblogging.


## Status

This project is still in its early days.
Super duper totes work in progress.
Lots to be done to be even a little bit useful.
There's no launched version anywhere yet, though hopefully that'll change Soon™.

Please keep in mind that much of the project is still under consideration.
The features, interface, etc.
are all still very much subject to change.


## Overview

You install Microblot into your Slack workspace and get `/microblot`, which lets you
create, list, edit, and delete posts on a blog specific to said workspace.
Chat is the only management interface, and the blog and associated feed are publicly
available.
Workspace admins are able to manage all posts, and other users only their own.

Note: At some point there may be a master blog, including content from all public blogs.
See [issue #55](https://github.com/nkantar/Microblot/issues/55).

E.g., if you install Microblot into the _My Extra Cool Team_ workspace,
`/microblot [new|list|edit|delete|info|help]` will manage posts on
`https://myextracoolteam.microblot.io`.


## Interface

All Microblot interaction (save for the installation into the workspace and removal
therefrom) happens through chat itself:

- `/microblot new` opens a modal with fields for the post title, body, and category.
  Submitting publishes the post.
- `/microblot list` lists relevant posts with their IDs.
  "Relevant" is defined as "all" for admins and "own" for all other users.
- `/microblot edit <ID>` opens the aforementioned modal prefilled with post content.
  Submitting updates the post.
  Only allowed for relevant posts.
- `/microblot delete <ID>` deletes the post.
  Only allowed for relevant posts.
- `/microblot info` outputs blog metadata, e.g., main URL, feed URL, content download
  URL, stats.
- `/microblot help` displays something like this section.
- `/microblot` defaults to `/microblot help`.


## Purpose

I like microblogs.
They're neat for sharing short snippets of content.
A good example (_not_ using Microblot) is
[Hashrocket - Today I Learned](https://til.hashrocket.com/).
I want to be able to manage one without having to interact with it as an actual website
or repo.
I already share these kinds of things on various Slack teams throughout the day, so may
as well publish for the world to see.


## (Anticipated) FAQ

- **Will other platforms be supported?** Sure, if someone contributes support for them.
  I plan on genericizing the interaction between the Slack API piece and the site
  content pieces to support that, but I don't personally have a need for this to run
  anywhere else.
  Voice your request in an [issue](https://github.com/nkantar/Microblot/issues), though,
  and we'll see what happens.
- **How do you plan on making the project sustainable?** Honestly, I'm not sure yet.
  I've got some ideas for features that would make sense in a paid tier (see
  [issue #57](https://github.com/nkantar/Microblot/issues/57)), I'd happily accept
  donations (for hosting costs at least, once it's up and running), and I'm open to
  other suggestions.
- **Is it cool if I run it myself?** Sure! Due to resource (read: time) constraints, I
  don't plan on investing a whole lot into making the project easily runnable anywhere
  other than the main deployment, but I'm not at all against it.
  Start a conversation in an [issue](https://github.com/nkantar/Microblot/issues) and
  let's see what we can do.
- **Why Python/Django?** Because I like it.
- **Why Heroku instead of own server or cloud?** Least amount of effort and maintenance
  by a long shot.


## Contributing

While it's probably a bit early for you to start contributing code, I'd love to know
what people think about this.
I've also got some
[questions](https://github.com/nkantar/Microblot/issues?q=is%3Aopen+is%3Aissue+label%3Atype%3Aquestion)
I specifically still want to think through on which feedback is welcome.
If you'd rather get in touch with me privately, you can try
[email](mailto:nik@nkantar.com) or [Twitter](https://twitter.com/nkantar).

Please note that this project is released with a
[Contributor Code of Conduct](https://github.com/nkantar/Microblot/blob/master/CODE_OF_CONDUCT.md).
By participating in this project you agree to abide by its terms.
(See [issue #88](https://github.com/nkantar/Microblot/issues/88).)


## License

This software is licensed under the _MIT License_.
Please see the included `LICENSE` file for details.
