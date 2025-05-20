from PIL import Image
import os
import math

# KONFIGURATION
icon_folder = "png"           # Ordner mit PNG-Dateien
output_file = "preview_2.png"     # Dateiname des Outputs
icons_per_row = 10               # Anzahl Icons pro Zeile
icon_size = (64, 64)            # Icon-Größe

# ICONS LADEN
png_files = [f for f in os.listdir(icon_folder) if f.lower().endswith(".png")]
total_icons = len(png_files)
rows = math.ceil(total_icons / icons_per_row)

# LEERES BILD ANLEGEN
preview_width = icons_per_row * icon_size[0]
preview_height = rows * icon_size[1]
preview = Image.new("RGBA", (preview_width, preview_height), (255, 255, 255, 0))

# ICONS EINSETZEN
for i, filename in enumerate(sorted(png_files)):
    path = os.path.join(icon_folder, filename)
    icon = Image.open(path).convert("RGBA").resize(icon_size, Image.NEAREST)  # scharfe Pixel!
    x = (i % icons_per_row) * icon_size[0]
    y = (i // icons_per_row) * icon_size[1]
    preview.paste(icon, (x, y), icon)

# SPEICHERN
preview.save(output_file)
print(f"✅ Vorschau gespeichert als: {output_file}")
