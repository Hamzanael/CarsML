options_title = [
    'ABS',
    'Xenon Light',
    'Leather Seats',
    'Touch Screen',
    'Navigation System',
    'Led Lights',
    'Sunroof',
    'Heated Seats',
    'Bluetooth',
    'Electric mirrors',
    'Cruise Control',
    'Rear camera',
    'Parking sensors',
]

for title in options_title:
    print(f'''
        <div style = "float: left">
            <input class="form-check-input" style="margin-left:1rem" type="checkbox" value="{title}">
            <label class="form-label">{title}</label>   
        </div>
    ''')
    # print(f'<input class="form-check-input" style="margin-left:1rem" type="checkbox" value="{title}">')
    # print(f'<label class="form-label">{title}</label>')
