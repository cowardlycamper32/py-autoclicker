import windows_toasts as wts

toaster = wts.WindowsToaster("python")
toast = wts.Toast()
toast.text_fields = ["Hello World!"]
icon = wts.ToastDisplayImage.fromPath("icon.ico")
showFor = wts.ToastDuration.Short
toast.images = [icon]
toast.duration = showFor
toaster.show_toast(toast)