from wtforms import ValidationError


def length_check(max_len=6, min_len=5):
    if max_len <= min_len:
        max_len, min_len = 6, 5

    def _length_check(form, field):
        print(str(field.data))
        if min_len > len(str(field.data)) or max_len < len(str(field.data)):
            raise ValidationError(
                f"Поле должно быть не меньше {min_len}-и и не больше {max_len}-и символов в длину.")

    return _length_check
