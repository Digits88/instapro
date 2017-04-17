from instabot.api.request import Request


def get_user_info(user, user_id):
    return Request.send(user.session, 'users/' + str(user_id) + '/info/')


def get_user_feed(user, user_id, maxid='', minTimestamp=None):
    return Request.send(user.session,
                        'feed/user/' + str(user_id) + '/?max_id=' + str(maxid) + '&min_timestamp=' + str(minTimestamp) +
                        '&rank_token=' + str(user.rank_token) + '&ranked_content=true')


def get_user_followers(user, user_id, maxid=''):
    return Request.send(user.session,
                        'friendships/' + str(user_id) + '/followers/?max_id=' + str(maxid) + '&rank_token=' + user.rank_token)


def get_user_following(user, user_id, maxid=''):
    return Request.send(user.session,
                        'friendships/' + str(user_id) + '/following/?max_id=' + str(maxid) + '&rank_token=' + str(user.rank_token))


def get_liked_media(user, maxid=''):
    return Request.send(user.session, 'feed/liked/?max_id=' + str(maxid))
