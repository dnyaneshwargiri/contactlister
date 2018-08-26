from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context,loader
from contactlisterapp.scrape_contacts import scrape_contact
# Create your views here.


'''class HomeView():
	templat_name="contactlisterapp/index.html"
	def get(self,request):
		form=Homeforms()
		return render(request,self.templat_name,{form:'form'})
		
	def post(self,request):
		if form.is_valid():
			text=form.cleaned_data['sitename']
			form=Homeforms()
			args={'form':form,'text':text}
		return render(request,self.templat_name,args)
'''
def index(request):
	if request.method=='POST':
		mylist=["" for x in range(300)]
		sitename=request.POST.get('sitename')
		print ("Sitename "+sitename)
		sc=scrape_contact()
		if sc.accept_url(sitename):
			mylist=sc.scrape_emails(sitename)
			flag=0;
			for ml in mylist:
				if ml:
					flag=1;
			if mylist and flag==1 :
				msg='Theses Are The Contacts For :'
				context={'resultforsitename':sitename,'mylist':mylist,'message':msg}
				return render(request,'index.html',context)
				
			else :
				msg='No Contacts  For :'
				context={'resultforsitename':sitename,'mylist':mylist,'message':msg};
				#return render(request,'index.html',context)
			
		

	#template=loader.get_template("contactlisterapp/index.html")
	return render(request,'index.html')


	
