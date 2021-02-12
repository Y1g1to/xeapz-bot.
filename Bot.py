import discord
from discord.enums import Status
from discord.ext import commands, tasks
from discord.ext.commands.core import command
import json
import typing
from random import randint
from random import choice





client = commands.Bot(command_prefix = "=")


status = ["Geliştiricim: yi#7927", "Bot Geliştiriliyor...", "Bu Bot Xeapz Discord İçindir."]

@client.event
async def on_ready():
    change_status.start()
    
    
    print("Bot Is Online!")
    
@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="gelen-giden")
    await channel.send(f"{member} Aramıza Katıldı! Hoşgeldin! :sparkles:")
    
    print(f"{member} Aramıza Katıldı. Hoşgeldin!")
    
@client.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name="gelen-giden")
    await channel.send(f"{member} Aramızdan Ayrıldı :(. Görüşürüz. :pensive:")
    print(f"{member} Aramızdan Ayrıldı :(. Görüşürüz.")

        
        
@tasks.loop(seconds=20)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))
    
          

    
@client.command(aliases=["gelistirici", "Geliştirici", "geliştirici"])

async def Gelistirici(ctx):
    embed = discord.Embed(title = "Açıklama", description = "Geliştiricim: yi#7927", color = discord.Color.red())
    embed.add_field(name= "Açıklama", value="Bot Geliştiriliyor...", inline=True)
    await ctx.send(embed=embed)

@client.command(aliases=["yardım", "yardim", "Yardım"])
async def Yardim(ctx):
    embed = discord.Embed(title="Yardım!", color=discord.Color.green(), description ="**=kick <Kickleyeceginiz Kisi> <Nedeni>  : Kickleyeceğiniz Kisiyi Etiketlediginiz Zaman Kisi Sunucudan Atilir.Bu Komutu Kendi Rolunden Yuksek Birinde Kullanamassin \n \n =ban <Banlayacaginiz Kisi> <Nedeni> : Banlayacaginiz Kisiyi Etiketlediginiz Zaman Kisi Sunucudan Banlanir.Bu Komutu Kendi Rolunden Yuksek Birinde Kullanamassin. \n \n =YasagiKaldir <Yasagi Kaldiracaginiz Kisi> : Yasagi Kaldiracaginiz Kisiyi Etiketlediginiz Zaman Kisi Sunucudan Unbanlanir. \n  \n =sil <ne kadar silsin> : Belirlediginiz Miktar Kadar Mesaj Siler.. \n \n =sayi <sayi> : Belirlediginiz Miktar Kadar Random Sayi Uretir. (max 1 ile 1000 arasinda bir sayi secebilirsiniz. \n \n =rolekle <rol> <kullanici> Kullaniciya Etiketlediginiz Rolu Verir. \n \n =rolsil <rol> <kullanici> Kullanicinin Rollerinden Etiketlediginiz Rolu Siler. \n \n =guncellemenotu Bota Gelen Guncellemeleri Burda Gorebilirsiniz! \n \n =kullanıcı <üye> Kullanıcının Bilgilerini Gösterir. \n \n =sil_rol <rol> <nedeni> Etiketlediğiniz Rolu Siler. \n\n =rol-oluştur <rolismi> <rol rengi> <nedeni> Sunucudaki Rollere Yeni Bir Rol Ekler. \n \n =rol-pozisyon <rol> <pozisyon> Etiketlediğiniz Rolu Belirlediğiniz Pozisyona Çeker.**")
    
    
    embed.set_footer(text="Beni Kullandığınız İçin Teşekkür Ederim!", icon_url=client.user.avatar_url)

    
    await ctx.send(embed=embed)
    
@client.command(aliases=["güncellemenotu", "Güncellemenotu", "güncellemeNotu", "GüncellemeNotu", "Guncellemenotu","guncellemeNotu", "GuncellemeNotu"])
async def guncellemenotu(ctx):
    embed = discord.Embed(title="Güncelleme Notu!", color=discord.Color.green(), description="** [9-02-2021] \n Botun Gönderdiği Yazılar Artık Embed Olacak! \n \n 2- =kullanıcı Komutu Eklendi \n \n sil_rol Komutu Geldi! \n \n rol-oluştur Komutu Geldi!\n\n Rol-Pozisyon Komutu Geldi!**")
    
    
    embed.set_footer(text="Beni Kullandığınız İçin Teşekkür Ederim!", icon_url=client.user.avatar_url)
 
    
    await ctx.send(embed=embed)

@client.command(aliases=["Kick"])
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member,*,reason):
        await member.kick(reason=reason)
        embed = discord.Embed(title="Kick", color=discord.Color.green(), description="**{}, {} Nedeniyle Sunucudan Atıldı.**".format(member.name, reason))
        embed.set_footer(text="Beni Kullandığınız İçin Teşekkür Ederim!", icon_url=client.user.avatar_url)
        
        await ctx.send(embed=embed)
@kick.error
async def kick_error(ctx, error):
    
    
    if isinstance(error, commands.MissingRequiredArgument):
        embed1 = discord.Embed(title="Argument Hatası", color=discord.Color.green(), description="**Lütfen Geçerli Bir Üye Yada Neden Seçin.**")
        embed1.set_footer(text="Beni Kullandığınız İçin Teşekkür Ederim!", icon_url=client.user.avatar_url)
        await ctx.send(embed=embed1)
    elif isinstance(error, commands.MissingPermissions):
        embed2 = discord.Embed(title="Permissions Hatası", color=discord.Color.green(), description="**Bu Komutu Kullanabilmek İçin Yeterli Yetkiniz Yok.**")
        embed2.set_footer(text="Beni Kullandığınız İçin Teşekkür Ederim!", icon_url=client.user.avatar_url)
        await ctx.send(embed=embed2)
        
        


@client.command(aliases=["Ban"])
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member,*,reason):
        await member.ban(reason=reason)
        embed = discord.Embed(title="Ban", color=discord.Color.green(), description="**{}, {} Nedeniyle Sunucudan Yasaklandı.**".format(member.name, reason))
        embed.set_footer(text="Beni Kullandığınız İçin Teşekkür Ederim!", icon_url=client.user.avatar_url)
        
        await ctx.send(embed=embed)
               
@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed1 = discord.Embed(title="Argument Hatası", color=discord.Color.green(), description="**Lütfen Geçerli Bir Üye Yada Neden Seçin.**")
        embed1.set_footer(text="Beni Kullandığınız İçin Teşekkür Ederim!", icon_url=client.user.avatar_url)
        await ctx.send(embed=embed1)
    elif isinstance(error, commands.MissingPermissions):
        embed2 = discord.Embed(title="Permissions Hatası", color=discord.Color.green(), description="**Bu Komutu Kullanabilmek İçin Yeterli Yetkiniz Yok.**")
        embed2.set_footer(text="Beni Kullandığınız İçin Teşekkür Ederim!", icon_url=client.user.avatar_url)
        await ctx.send(embed=embed2)
        


@client.command(aliases=["purge", "Purge", "delete", "Delete", "clear", "Clear", "Sil"])
@commands.has_permissions(manage_messages=True)
async def sil(ctx, amount):
     await ctx.channel.purge(limit=int(amount))
@sil.error
async def sil_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed1 = discord.Embed(title="Argument Hatası", color=discord.Color.green(), description="**Lütfen Geçerli Bir Miktar Seçin.**")
        embed1.set_footer(text="Beni Kullandığınız İçin Teşekkür Ederim!", icon_url=client.user.avatar_url)
        await ctx.send(embed=embed1)
    elif isinstance(error, commands.MissingPermissions):
        embed2 = discord.Embed(title="Permissions Hatası", color=discord.Color.green(), description="**Bu Komutu Kullanabilmek İçin Yeterli Yetkiniz Yok.**")
        embed2.set_footer(text="Beni Kullandığınız İçin Teşekkür Ederim!", icon_url=client.user.avatar_url)
        await ctx.send(embed=embed2)

@client.command(aliases=["Yasagikaldir", "yasagıkaldır", "YasagıKaldır", "Yasagıkaldır", "yasagıKaldır", "YasagiKaldir","YasağıKaldır"])

@commands.has_permissions(ban_members=True)
async def yasagikaldir(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name,member_discriminator = member.split('#')
    
    for ban_entry in banned_users:
       user = ban_entry.user
       
       if (user.name, user.discriminator) == (member_name, member_discriminator):
           await ctx.guild.unban(user) 
           embed = discord.Embed(title="*Unban", color=discord.Color.green(), description="**{}, Sunucudan Yasağı Kaldırıldı**".format(member.name))
           embed.set_footer(text="Beni Kullandığınız İçin Teşekkür Ederim!", icon_url=client.user.avatar_url)
        
           await ctx.send(embed=embed)
           return
@yasagikaldir.error
async def unban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed1 = discord.Embed(title="Argument Hatası", color=discord.Color.green(), description="**Lütfen Geçerli Bir Üye Yada Neden Seçin.**")
        embed1.set_footer(text="Beni Kullandığınız İçin Teşekkür Ederim!", icon_url=client.user.avatar_url)
        await ctx.send(embed=embed1)
    elif isinstance(error, commands.MissingPermissions):
        embed2 = discord.Embed(title="Permissions Hatası", color=discord.Color.green(), description="**Bu Komutu Kullanabilmek İçin Yeterli Yetkiniz Yok.**")
        embed2.set_footer(text="Beni Kullandığınız İçin Teşekkür Ederim!", icon_url=client.user.avatar_url)
        await ctx.send(embed=embed2)
         
     
@client.command(aliases=["sayi", "sayı", "Sayı"])
async def Sayi(ctx, arg1):
    if (int(arg1) <= 1000) and (int(arg1) > 0):
        embed = discord.Embed(title="Sayı", color=discord.Color.green(), description="**Sayınız: {}**".format(int(arg1)))
        embed.set_footer(text="Beni Kullandığınız İçin Teşekkür Ederim!", icon_url=client.user.avatar_url)
        
        await ctx.send(embed=embed)
    else:
        embed1 = discord.Embed(title="Sayı Hatası", color=discord.Color.green(), description="**Lütfen 1 İle 1000 Arasında Bir Sayı Girin.**")
        embed1.set_footer(text="Beni Kullandığınız İçin Teşekkür Ederim!", icon_url=client.user.avatar_url)
        
        await ctx.send(embed=embed1)        
@Sayi.error
async def Sayi_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed1 = discord.Embed(title="Sayı Hatası", color=discord.Color.green(), description="**Lütfen Geçerli Bir Sayı Seçin.**")
        embed1.set_footer(text="Beni Kullandığınız İçin Teşekkür Ederim!", icon_url=client.user.avatar_url)
        
        await ctx.send(embed=embed1)
        
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title="Komut Hatası", color=discord.Color.green(), description="**Hatalı Komut. Botta Böyle Bir Komut Yok. Komutları Öğrenmek İstersen: =yardım**")
        embed.set_footer(text="Beni Kullandığınız İçin Teşekkür Ederim!", icon_url=client.user.avatar_url)
        
        await ctx.send(embed=embed)

@client.command(aliases=["Rolekle", "rolEkle", "ROLEKLE"])
@commands.has_permissions(administrator=True)
async def rolekle(ctx, role: discord.Role, user: discord.Member):
    await user.add_roles(role)
    embed1 = discord.Embed(title="Rol Ekle", color=discord.Color.green(), description= f"**{user.mention} Kullanıcısına Başarılı Bir Şekilde {role.mention} Rolu Verildi!**")
    embed1.set_footer(text="Beni Kullandığınız İçin Teşekkür Ederim!", icon_url=client.user.avatar_url)
        
    await ctx.send(embed=embed1)
@rolekle.error 
async def rolekle_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed1 = discord.Embed(title="Argument Hatası", color=discord.Color.green(), description="**Lütfen Geçerli Bir Üye Yada Rol Seçin.**")
        embed1.set_footer(text="Beni Kullandığınız İçin Teşekkür Ederim!", icon_url=client.user.avatar_url)
        await ctx.send(embed=embed1)
    elif isinstance(error, commands.MissingPermissions):
        embed2 = discord.Embed(title="Permissons Hatası!", color=discord.Color.green(), description="**Bu Komutu Kullanabilmek İçin Yeterli Yetkiniz Yok.**")
        embed2.set_footer(text="Beni Kullandığınız İçin Teşekkür Ederim!", icon_url=client.user.avatar_url)
        await ctx.send(embed=embed2)
@client.command(aliases=["Rolsil", "rolSil", "ROLSİL", "ROLSIL"])
@commands.has_permissions(administrator=True)
async def rolsil(ctx, role: discord.Role, user: discord.Member):
    await user.remove_roles(role)
    embed1 = discord.Embed(title="Rol Sil", color=discord.Color.green(), description= f"**{user.mention} Kullanıcısının Başarılı Bir Şekilde {role.mention} Rolu Silindi!**")
    embed1.set_footer(text="Beni Kullandığınız İçin Teşekkür Ederim!", icon_url=client.user.avatar_url)
        
    await ctx.send(embed=embed1)

@rolsil.error 
async def rolsil_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed1 = discord.Embed(title="Argument Hatası", color=discord.Color.green(), description="**Lütfen Geçerli Bir Üye Yada Rol Seçin.**")
        embed1.set_footer(text="Beni Kullandığınız İçin Teşekkür Ederim!", icon_url=client.user.avatar_url)
        await ctx.send(embed=embed1)
    elif isinstance(error, commands.MissingPermissions):
        embed2 = discord.Embed(title="Permissons Hatası!", color=discord.Color.green(), description="**Bu Komutu Kullanabilmek İçin Yeterli Yetkiniz Yok.**")
        embed2.set_footer(text="Beni Kullandığınız İçin Teşekkür Ederim!", icon_url=client.user.avatar_url)
        await ctx.send(embed=embed2)        
@client.command(aliases=["kullanıcı", "Kullanıcı", "Kullanici"])
async def kullanici(ctx, member: typing.Optional[discord.Member]):
    if member == None:
        member = ctx.author

    if member.bot:
        kullanıcı_botmu = "Evet"
    else:
        kullanıcı_botmu = "Hayır"

    kullanıcı_id = member.id

    kullanici_rolleri_list = [r.mention for r in member.roles if r != ctx.guild.default_role]
    kullanici_butun_roller_fix = ", ".join(kullanici_rolleri_list)

    kullanici_sunucuya_giris_obj = str(member.joined_at)
    kullanici_bolunmus_sunucuya_giris = kullanici_sunucuya_giris_obj.split(".")
    kullanici_sunucuya_giris = kullanici_bolunmus_sunucuya_giris[0]

    kullanici_hesap_tarihi_obj = str(member.created_at)
    kullanici_bolunmus_hesap_tarihi = kullanici_hesap_tarihi_obj.split(".")
    kullanici_hesap_tarihi = kullanici_bolunmus_hesap_tarihi[0]

    embed = discord.Embed(title=f"{member.mention} Kişinin Detayları", description=f"**Kullanıcı ID:**\n{kullanıcı_id}\n\n**Bot mu?**\n{kullanıcı_botmu}\n\n**Roller ({len(kullanici_rolleri_list)}):**\n{kullanici_butun_roller_fix}\n\n**Sunucuya Giriş Tarihi (ABD):**\n{kullanici_sunucuya_giris}\n\n**Hesap Oluşturma Tarihi (ABD):**\n{kullanici_hesap_tarihi}", color=0xff00ff)
    embed.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed=embed)
    
@client.command(aliases = ['sil-rol', "Sil-rol", "Sil-Rol", "SİL-ROL", "SIL-ROL"])
@commands.has_permissions(manage_roles=True)
async def sil_rol(ctx,rol:discord.Role,*,reasonm = 'Sebepsiz'):

    await rol.delete(reason=reasonm)
    embed1 = discord.Embed(title="Rol Sil", color=discord.Color.green(), description= "{}, Adlı Rol {} Sebepiyle Silindi!".format(rol.mention, reasonm))
    
    embed1.set_footer(text="Beni Kullandığınız İçin Teşekkür Ederim!", icon_url=client.user.avatar_url)
        
    await ctx.send(embed=embed1)
    

@sil_rol.error 
async def silrol_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed1 = discord.Embed(title="Argument Hatası", color=discord.Color.green(), description="**Lütfen Geçerli Bir Sebep Yada Rol Seçin.**")
        embed1.set_footer(text="Beni Kullandığınız İçin Teşekkür Ederim!", icon_url=client.user.avatar_url)
        await ctx.send(embed=embed1)
    elif isinstance(error, commands.MissingPermissions):
        embed2 = discord.Embed(title="Permissons Hatası!", color=discord.Color.green(), description="**Bu Komutu Kullanabilmek İçin Yeterli Yetkiniz Yok.**")
        embed2.set_footer(text="Beni Kullandığınız İçin Teşekkür Ederim!", icon_url=client.user.avatar_url)
        await ctx.send(embed=embed2)        
@client.command(aliases=["rol-oluştur", "Rol-oluştur", "Rol-Oluştur", "ROL-OLUŞTUR"])
@commands.has_permissions(manage_roles=True)
async def rol_olustur(ctx,isim, color = discord.Colour(0xffffff),*, reasonm="Sebepsiz"):
    guild=ctx.guild
    await guild.create_role(name=str(isim), color=color)
    
    embed1 = discord.Embed(title="Rol Oluştur", color=discord.Color.green(), description= "{}, Adlı Rol {} Sebepiyle Oluşturuldu!".format(isim, reasonm))
    
    embed1.set_footer(text="Beni Kullandığınız İçin Teşekkür Ederim!", icon_url=client.user.avatar_url)
        
    await ctx.send(embed=embed1)    
    
@rol_olustur.error 
async def rol_olustur_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed1 = discord.Embed(title="Argument Hatası", color=discord.Color.green(), description="**Lütfen Geçerli Bir Sebep Yada Rol Seçin.**")
        embed1.set_footer(text="Beni Kullandığınız İçin Teşekkür Ederim!", icon_url=client.user.avatar_url)
        await ctx.send(embed=embed1)
    elif isinstance(error, commands.MissingPermissions):
        embed2 = discord.Embed(title="Permissons Hatası!", color=discord.Color.green(), description="**Bu Komutu Kullanabilmek İçin Yeterli Yetkiniz Yok.**")
        embed2.set_footer(text="Beni Kullandığınız İçin Teşekkür Ederim!", icon_url=client.user.avatar_url)
        await ctx.send(embed=embed2)
   
@client.command(aliases=["rol-pozisyon", "Rol-pozisyon", "Rol-Pozisyon", "ROL-POZİSYON"])
@commands.has_permissions(administrator=True)
async def rol_pozisyon(ctx, role: discord.Role, pos):
    try:
        await role.edit(position=int(pos))
        embed1 = discord.Embed(title="Rol Oluştur", color=discord.Color.green(), description= "{}, Adlı Rol {} Pozisyonuna Yerleştirildi!".format(role.mention, pos))
    
        embed1.set_footer(text="Beni Kullandığınız İçin Teşekkür Ederim!", icon_url=client.user.avatar_url)
        
        await ctx.send(embed=embed1) 
    except discord.Forbidden:
        embed2 = discord.Embed(title="Permissons Hatası!", color=discord.Color.green(), description="**Bu Komutu Kullanabilmek İçin Yeterli Yetkiniz Yok.**")
        embed2.set_footer(text="Beni Kullandığınız İçin Teşekkür Ederim!", icon_url=client.user.avatar_url)
        await ctx.send(embed=embed2)
    except discord.HTTPException:
        embed3 = discord.Embed(title="Hata!", color=discord.Color.green(), description="**Pozisyonu Ayarlarken Bir Hata Oluştu.**")
        embed3.set_footer(text="Beni Kullandığınız İçin Teşekkür Ederim!", icon_url=client.user.avatar_url)
        await ctx.send(embed=embed3)
    except discord.InvalidArgument:
        embed4 = discord.Embed(title="Hata!", color=discord.Color.green(), description="**Lütfen Geçerli Bir Pozisyon Yada Rol Ekleyin.**")
        embed4.set_footer(text="Beni Kullandığınız İçin Teşekkür Ederim!", icon_url=client.user.avatar_url)
        await ctx.send(embed=embed4)

        
        
client.run("ODA4MDY5MDQ1NzM1NjUzNDQ2.YCBK8Q.pvI7fYBLAv3dtpCB94XS40XK6OY")
