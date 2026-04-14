from api import TikTok

print(TikTok(session_id = "79ab1b7da619").following_list(
        user_id = 7473102865897849902,
        sec_user_id = "MS4wLjABAAAABEFxc5B6GNZslMi6uVdCWnHBfjuNQGeTkt9G8ffgDdSGgakRXh2ee7lgY0CMpOQQ",
        count = 125
    )
)
