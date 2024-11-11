from django.db import models



class MBS_system(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class MBS_project(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

    # def __str__(self):
    #     return f"{self.tag} - {self.name} ({self.param_type})"







class MBS_device_type(models.Model):
    value = models.CharField(max_length=100)
    system = models.ForeignKey(MBS_system, on_delete=models.DO_NOTHING)
    project = models.ForeignKey(MBS_project, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.value



class MBS_param_name(models.Model):
    name = models.CharField(max_length=50)
    device_type = models.ManyToManyField(MBS_device_type)

    def __str__(self):
        return self.name



class MBS_param_value(models.Model):
    value = models.TextField('Значение поля')
    name = models.ForeignKey(MBS_param_name, on_delete=models.CASCADE)
    incrementable = models.BooleanField('Инкрементируемый', default=False)
    init_increment_val = models.IntegerField('Начально значение инкремента')

    def __str__(self):
        return self.value




# class DeviceFieldRow(models.Model):
#     row_number = models.IntegerField('Порядковый номер')
#     device_tag = models.CharField(max_length=50, verbose_name='Обозначение')
#     param_name = models.CharField(max_length=100, verbose_name='Название параметра')

    






# {"№ п/п": row_number, "Обозначение": device.tag, "Переменная": device.name, "Элемент": "Значение", "Ед.изм": "мА", "Тип данных": "Real", "Чтение/Запись": "чтение", "Адрес Modbus": modbus_start},



class Device(models.Model):
    DEVICE_TYPES = [
        ('Аналоговый датчик', 'Аналоговый датчик'),
        ('Кран с электрическим приводом', 'Кран с электрическим приводом'),
        ('Электромагнитный клапан', 'Электромагнитный клапан'),
        ('Насос', 'Насос'),
    ]

    tag = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    param_type = models.CharField(max_length=50, choices=DEVICE_TYPES)

    def __str__(self):
        return f"{self.tag} - {self.name} ({self.param_type})"
