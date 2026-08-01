with open('index.html', 'r') as f:
    content = f.read()

# Restore top nav ENGAGE button
content = content.replace("switchTab('essay-1')\" id=\"tab-btn-engage\"", "switchTab('engage')\" id=\"tab-btn-engage\"")
content = content.replace("switchTab('essay-1'); toggleMobileMenu();\" class=\"block w-full py-2 bg-castine-gold", "switchTab('engage'); toggleMobileMenu();\" class=\"block w-full py-2 bg-castine-gold")
content = content.replace("onclick=\"switchTab('essay-1')\" class=\"bg-castine-gold hover:bg-castine-dark-gold text-castine-navy font-cinzel font-bold text-xs tracking-widest px-8 py-3 rounded-sm shadow-lg transition\">\n                            REQUEST A CONSTRAINT SCAN", "onclick=\"switchTab('engage')\" class=\"bg-castine-gold hover:bg-castine-dark-gold text-castine-navy font-cinzel font-bold text-xs tracking-widest px-8 py-3 rounded-sm shadow-lg transition\">\n                            REQUEST A CONSTRAINT SCAN")

# Target ONLY the Castine Papers essay button
old_essay_btn = 'READ FULL MONOGRAPH & REQUEST SCAN ➔'
new_essay_btn = 'READ ESSAY ➔'

if old_essay_btn in content:
    content = content.replace(old_essay_btn, new_essay_btn)

# Make sure the essay button points to essay-1
content = content.replace("onclick=\"switchTab('engage')\" class=\"text-xs font-cinzel text-castine-navy font-bold border-b border-castine-gold hover:text-castine-gold transition\">\n                            READ ESSAY ➔", "onclick=\"switchTab('essay-1')\" class=\"text-xs font-cinzel text-castine-navy font-bold border-b border-castine-gold hover:text-castine-gold transition\">\n                            READ ESSAY ➔")

with open('index.html', 'w') as f:
    f.write(content)

print("SUCCESS: Clean patch applied!")
