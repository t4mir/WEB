import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CategoriesComponent } from './categories/categories.component';
import { ProductsListComponent } from './products-list/products-list.component';
import { CompaniesComponent } from './companies/companies.component';
import { ToptenhotComponent } from './users/toptenhot.component';
import { LoginpageComponent } from './loginpage/loginpage.component';
import { GamesallComponent } from './gamesall/gamesall.component';

@NgModule({
  declarations: [
    AppComponent,
    CategoriesComponent,
    ProductsListComponent,
    CompaniesComponent,
    ToptenhotComponent,
    LoginpageComponent,
    GamesallComponent
],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { 
  // HttpClientModule,
  // HttpClientInMemoryWebApiModule.forRoot(
  //   InMemoryDataService, { dataEncapsulation: false }
  // )

}
