import traceback
import includes.main

async def main(ctx, prgm, console):
    # Python program using
    # traces to kill threads

    import sys
    import trace
    import threading
    import time
    class thread_with_trace(threading.Thread):
        def __init__(self, *args, **keywords):
            threading.Thread.__init__(self, *args, **keywords)
            self.killed = False

        def start(self):
            self.__run_backup = self.run
            self.run = self.__run
            threading.Thread.start(self)

        def __run(self):
            sys.settrace(self.globaltrace)
            self.__run_backup()
            self.run = self.__run_backup

        def globaltrace(self, frame, event, arg):
            if event == 'call':
                return self.localtrace
            else:
                return None

        def localtrace(self, frame, event, arg):
            if self.killed:
                if event == 'line':
                    raise SystemExit()
            return self.localtrace

        def kill(self):
            self.killed = True

    def func():
        print(threading.get_ident())
        with open("messages/message"+str(threading.get_ident())+".py","w") as message:
            message.write(prgm.content)
        with open("retours/retour"+str(threading.get_ident())+".txt","a") as retour:
            retour.write(str(ctx.message.guild.id)+"\n")
            retour.write(str(ctx.message.channel.id)+"\n")
            retour.write(str(ctx.message.author.id)+"\n")
            sys.stdout = retour
            fichier = "messages/message"+str(threading.get_ident())+".py"
            try:
                exec(open(fichier).read(),{})
            except SystemExit:
                pass
            except:
                retour.write(''.join(traceback.format_exception(*sys.exc_info())))
        sys.stdout = console
        with open("listeretour.txt","w") as listeretour:
            listeretour.write(str(threading.get_ident())+"\n")



    t1 = thread_with_trace(target=func)
    t1.start()
    time.sleep(includes.constants.delai)
    if t1.is_alive():
        t1.kill()
        await ctx.send("Votre programme a mis plus de "+str(includes.constants.delai)+" secondes à s'éxecuter. Ralentissez le.")
    t1.join()
