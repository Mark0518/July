import 'hammerjs';
import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {FormsModule} from '@angular/forms';
import {HttpModule} from '@angular/http';
import {AppRoutingModule} from './app-routing.module';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';

// Component
import {AppComponent} from './app.component';
import {BlogComponent} from './blog/blog.component';
import {NotFoundComponent} from './not-found/not-found.component';
import {FooterComponent} from './footer/footer.component';
import {HeaderComponent} from './header/header.component';
import {ArticleListComponent} from './article-list/article-list.component';
import { RightInfoComponent } from './right-info/right-info.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';

// Covalent
import { CovalentLayoutModule, CovalentStepsModule, CovalentPagingModule, CovalentMenuModule, CovalentSearchModule } from '@covalent/core';
// (optional) Additional Covalent Modules imports
import { CovalentHighlightModule } from '@covalent/highlight';
import { CovalentMarkdownModule } from '@covalent/markdown';
import { CovalentDynamicFormsModule } from '@covalent/dynamic-forms';

// Material
import { MaterialModule } from '@angular/material';
import { ArticleComponent } from './article/article.component';


@NgModule({
  declarations: [
    AppComponent,
    BlogComponent,
    NotFoundComponent,
    FooterComponent,
    HeaderComponent,
    ArticleListComponent,
    RightInfoComponent,
    LoginComponent,
    RegisterComponent,
    ArticleComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    // Covalent
    CovalentLayoutModule,
    CovalentStepsModule,
    CovalentHighlightModule,
    CovalentMarkdownModule,
    CovalentDynamicFormsModule,
    CovalentPagingModule,
    CovalentMenuModule,
    CovalentSearchModule,
    // Material
    MaterialModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {
}
