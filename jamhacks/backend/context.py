def user_context(request):  # so we can use {{ user }} in templates without passing every time
    user = request.session.get("user")
    print(user)
    if user is None:
        return {}
    return {'user': user}
