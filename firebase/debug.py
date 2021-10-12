from firebase import article
from firebase import schema
from firebase import user


def debug_user():
    try:
        try:
            return user.login("debug@debug.com", "debug1234")
        except:
            return user.register("debug@debug.com", "debug1234",
                                 "ada lovelace")
    except:
        raise Exception('debug user auth. failed.')


def test_articles():
    import random
    cover_list = [
        'https://i.imgur.com/eRM6hHb.jpeg', 'https://i.imgur.com/2k8WNSM.jpeg',
        'https://i.imgur.com/LEbNkdn.jpeg'
    ]
    for i in range(50):
        article.upload_article(
            schema.article(title=f'{i + 1}- Article title',
                           body=str("""
                
                # This is a title
                
                * hello there *
                
                - list
                - list
                - list         

                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse consectetur sit amet sapien non lobortis. In hac habitasse platea dictumst. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vivamus iaculis pharetra dolor, ullamcorper volutpat elit. Morbi a purus a justo interdum consequat. Nam iaculis ante vel augue aliquam, at volutpat lacus lacinia. Fusce tempus ligula sit amet mauris lacinia varius.

                Morbi nulla nulla, tempor aliquet tellus eu, suscipit scelerisque nisi. Nunc sagittis ultrices arcu, ac fermentum lacus facilisis sit amet. Vivamus hendrerit tempus nunc sit amet maximus. Sed velit turpis, tristique vel metus id, aliquet fermentum nibh. Nulla finibus, enim quis sollicitudin commodo, ex orci semper tellus, a porta eros mi sit amet tellus. Phasellus commodo a mauris nec laoreet. Vivamus rutrum lorem eu ex faucibus scelerisque. Proin ac turpis nec urna vestibulum pulvinar. Suspendisse et nisl ultrices, tristique elit sed, viverra est. Vivamus eu tortor at dolor feugiat aliquet. Sed nec ornare purus. Etiam laoreet mi leo, vitae pharetra sapien congue egestas.

                Morbi ullamcorper ipsum et feugiat pharetra. Aliquam bibendum pharetra mauris id mollis. Praesent pulvinar eleifend bibendum. Ut dapibus tempus odio non rutrum. In nec vestibulum magna. Nam lectus nunc, ultrices ut dapibus dignissim, molestie non turpis. Mauris quis metus dui. Aliquam sodales sapien vel felis aliquam feugiat. Pellentesque in risus justo. Vestibulum malesuada ornare sem. Nullam pulvinar dapibus mi, et cursus enim dapibus at. Nunc viverra dui neque, at efficitur ligula posuere vel. Proin sagittis odio dui, ac ultricies est iaculis maximus. Pellentesque sed faucibus est, ut interdum nibh.

                Etiam eu lobortis lorem, eu mattis odio. Sed convallis augue sit amet ipsum gravida congue. Curabitur vehicula mi id felis condimentum luctus. Fusce in ligula luctus, tempus lectus sed, ultrices felis. Aenean metus lacus, tempor sit amet fermentum sed, cursus in libero. Cras at ligula vel leo rutrum lacinia vitae non diam. Sed luctus sed libero eget tempus.

                Sed imperdiet diam sem. Vestibulum ac nunc commodo, consequat sapien in, tempus eros. Morbi mattis sit amet massa in pulvinar. Duis aliquam velit eu nisi gravida, sit amet pellentesque velit tincidunt. Suspendisse congue ex velit, id porttitor quam rutrum a. Suspendisse lacinia sem id erat ornare, quis volutpat neque posuere. Sed condimentum ultricies diam eget posuere. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus sollicitudin quam vitae ex porttitor, eget tempus dui elementum. Sed sit amet nulla egestas, auctor mi quis, placerat quam. Vestibulum tempor orci vitae condimentum condimentum.

                Nam quis felis non turpis congue gravida quis eu ante. Fusce fermentum sit amet lacus ut iaculis. Proin eu odio sit amet orci maximus condimentum. Quisque pretium diam venenatis elementum eleifend. Aenean posuere dui in ipsum pulvinar commodo. Integer ut ante quis lectus sollicitudin luctus at posuere nulla. In in mollis lacus, sit amet finibus tortor.

                Nam volutpat tortor id ex pellentesque, vel consectetur enim commodo. Morbi dapibus libero eu lorem aliquam, vitae pharetra orci elementum. Nunc eu nisl arcu. Sed sit amet malesuada ipsum. Pellentesque malesuada, purus a dictum pellentesque, risus est egestas lorem, sed facilisis sapien velit quis libero. Maecenas nec velit commodo, imperdiet massa quis, eleifend est. Nullam nisi magna, lobortis non faucibus vitae, ornare in turpis. Proin pharetra arcu non risus ornare, eget euismod magna semper.

                Cras consectetur dui id sagittis hendrerit. Fusce velit arcu, eleifend in tristique eu, tincidunt in sapien. Phasellus cursus ante at mi tincidunt, sed porttitor sapien cursus. Duis feugiat pharetra mi, et pellentesque velit tincidunt ut. Ut cursus eu erat sit amet tristique. Sed euismod enim nec mauris pellentesque, sit amet dictum leo congue. Vivamus ultricies ullamcorper blandit. Duis porta eget dolor a malesuada. Ut vel egestas leo, et tempus ipsum. Nam commodo malesuada arcu mattis suscipit. In semper, turpis non sagittis bibendum, metus leo dictum est, sit amet venenatis diam odio et diam. Aliquam nulla nisi, fringilla vitae purus vel, venenatis dignissim mauris.

                Vivamus faucibus porta vulputate. Nam mollis ullamcorper felis, vel luctus ligula iaculis vel. Mauris velit justo, pellentesque non tincidunt et, pellentesque sit amet ligula. Quisque et diam lacus. Nulla feugiat, purus ac euismod laoreet, tortor neque rhoncus risus, in venenatis nisl purus in massa. Aliquam in tincidunt elit. Etiam sagittis nisl sed sem consequat sodales. Aenean convallis leo eu odio ultrices viverra vel ac orci. Donec facilisis lacus dui. Curabitur viverra venenatis ante ut tristique. Aenean aliquet ligula est, sed consectetur justo pellentesque sed. Sed sit amet rhoncus nisi. Phasellus a lobortis lorem, sit amet gravida sem. Proin id aliquet turpis. Nulla in dui sed diam aliquam pulvinar id et urna.

                Maecenas commodo laoreet ligula vel aliquam. Maecenas molestie viverra arcu, a imperdiet sapien molestie congue. Donec nec lobortis quam. Aenean vitae dolor vitae enim consequat lobortis. Morbi sagittis risus vitae sollicitudin volutpat. Donec varius bibendum erat, sed blandit dui consequat ut. Proin laoreet justo arcu, eget pretium enim vulputate quis. Integer suscipit lorem eget tortor vehicula, et malesuada nulla rutrum. Duis vitae lorem ligula. Curabitur eu metus congue, commodo felis sit amet, bibendum nunc. Maecenas malesuada libero in risus dictum pharetra. Fusce vulputate ornare lorem sed ultricies. Duis vitae eros et neque sagittis faucibus. Nulla aliquam viverra convallis.

                Nunc orci tortor, rhoncus id augue id, porta elementum nunc. Donec egestas dolor non nisi aliquam mattis. Ut euismod porta dui, quis imperdiet metus. Integer a commodo neque. Phasellus id felis suscipit, pretium libero tempor, ornare est. Suspendisse sed suscipit lectus. Vivamus a condimentum felis, vitae aliquam libero. Quisque ligula mauris, molestie id luctus sed, interdum id magna. Aliquam volutpat viverra dictum. Vivamus libero felis, fringilla at lobortis varius, aliquam vitae nunc. Suspendisse quis consectetur justo, vitae sagittis nisl. Fusce lacinia sed leo id dictum. Vivamus eu nibh vehicula, rhoncus ligula ut, aliquam sapien.

                Etiam quam odio, mattis nec elit in, accumsan fermentum magna. Curabitur eget nisl vel nisi mollis laoreet non efficitur leo. Curabitur nec enim lacus. Nunc non facilisis lectus. Duis eu dolor massa. Vivamus tincidunt odio cursus est bibendum, at lacinia quam tempor. Ut arcu ante, egestas ac tempus a, convallis et ex. Pellentesque sit amet felis condimentum, maximus ex consectetur, feugiat diam. Nam aliquet velit sit amet finibus dignissim. Morbi in orci egestas, gravida mi eget, aliquam odio. Interdum et malesuada fames ac ante ipsum primis in faucibus. Donec massa diam, dapibus fermentum rhoncus et, consequat vel mi.

                """),
                           cover_image=random.choice(cover_list)))
