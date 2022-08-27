﻿/********************************
 * Super Stop N Buy
 * AdminManagerAdd.Designer.cs
 * Created by Justin Leonard
 * < Other Names Omitted >
********************************/

namespace SuperStopNBuy
{
    partial class AdminManagerAdd
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(AdminManagerAdd));
            this.buttonSaveAndExit = new System.Windows.Forms.Button();
            this.labelUsername = new System.Windows.Forms.Label();
            this.textboxUsername = new System.Windows.Forms.TextBox();
            this.labelAccessLevel = new System.Windows.Forms.Label();
            this.labelLastName = new System.Windows.Forms.Label();
            this.labelFirstName = new System.Windows.Forms.Label();
            this.textboxLastName = new System.Windows.Forms.TextBox();
            this.textboxFirstName = new System.Windows.Forms.TextBox();
            this.buttonBack = new System.Windows.Forms.Button();
            this.labelViewDetails = new System.Windows.Forms.Label();
            this.labelPassword = new System.Windows.Forms.Label();
            this.textboxPassword = new System.Windows.Forms.TextBox();
            this.comboBoxAccessLevel = new System.Windows.Forms.ComboBox();
            this.SuspendLayout();
            // 
            // buttonSaveAndExit
            // 
            this.buttonSaveAndExit.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F);
            this.buttonSaveAndExit.Location = new System.Drawing.Point(205, 358);
            this.buttonSaveAndExit.Margin = new System.Windows.Forms.Padding(2);
            this.buttonSaveAndExit.Name = "buttonSaveAndExit";
            this.buttonSaveAndExit.Size = new System.Drawing.Size(296, 64);
            this.buttonSaveAndExit.TabIndex = 6;
            this.buttonSaveAndExit.Text = "Save and Exit";
            this.buttonSaveAndExit.UseVisualStyleBackColor = true;
            this.buttonSaveAndExit.Click += new System.EventHandler(this.buttonSaveAndExit_Click);
            // 
            // labelUsername
            // 
            this.labelUsername.AutoSize = true;
            this.labelUsername.BackColor = System.Drawing.Color.Transparent;
            this.labelUsername.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F);
            this.labelUsername.Location = new System.Drawing.Point(226, 139);
            this.labelUsername.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.labelUsername.Name = "labelUsername";
            this.labelUsername.Size = new System.Drawing.Size(97, 24);
            this.labelUsername.TabIndex = 0;
            this.labelUsername.Text = "Username";
            // 
            // textboxUsername
            // 
            this.textboxUsername.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.textboxUsername.Location = new System.Drawing.Point(338, 142);
            this.textboxUsername.Margin = new System.Windows.Forms.Padding(2);
            this.textboxUsername.MaxLength = 32;
            this.textboxUsername.Name = "textboxUsername";
            this.textboxUsername.Size = new System.Drawing.Size(163, 21);
            this.textboxUsername.TabIndex = 1;
            // 
            // labelAccessLevel
            // 
            this.labelAccessLevel.AutoSize = true;
            this.labelAccessLevel.BackColor = System.Drawing.Color.Transparent;
            this.labelAccessLevel.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F);
            this.labelAccessLevel.Location = new System.Drawing.Point(201, 295);
            this.labelAccessLevel.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.labelAccessLevel.Name = "labelAccessLevel";
            this.labelAccessLevel.Size = new System.Drawing.Size(122, 24);
            this.labelAccessLevel.TabIndex = 0;
            this.labelAccessLevel.Text = "Access Level";
            // 
            // labelLastName
            // 
            this.labelLastName.AutoSize = true;
            this.labelLastName.BackColor = System.Drawing.Color.Transparent;
            this.labelLastName.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F);
            this.labelLastName.Location = new System.Drawing.Point(224, 256);
            this.labelLastName.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.labelLastName.Name = "labelLastName";
            this.labelLastName.Size = new System.Drawing.Size(99, 24);
            this.labelLastName.TabIndex = 0;
            this.labelLastName.Text = "Last Name";
            // 
            // labelFirstName
            // 
            this.labelFirstName.AutoSize = true;
            this.labelFirstName.BackColor = System.Drawing.Color.Transparent;
            this.labelFirstName.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F);
            this.labelFirstName.Location = new System.Drawing.Point(222, 217);
            this.labelFirstName.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.labelFirstName.Name = "labelFirstName";
            this.labelFirstName.Size = new System.Drawing.Size(101, 24);
            this.labelFirstName.TabIndex = 0;
            this.labelFirstName.Text = "First Name";
            // 
            // textboxLastName
            // 
            this.textboxLastName.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.textboxLastName.Location = new System.Drawing.Point(338, 259);
            this.textboxLastName.Margin = new System.Windows.Forms.Padding(2);
            this.textboxLastName.MaxLength = 32;
            this.textboxLastName.Name = "textboxLastName";
            this.textboxLastName.Size = new System.Drawing.Size(163, 21);
            this.textboxLastName.TabIndex = 4;
            // 
            // textboxFirstName
            // 
            this.textboxFirstName.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.textboxFirstName.Location = new System.Drawing.Point(338, 220);
            this.textboxFirstName.Margin = new System.Windows.Forms.Padding(2);
            this.textboxFirstName.MaxLength = 32;
            this.textboxFirstName.Name = "textboxFirstName";
            this.textboxFirstName.Size = new System.Drawing.Size(163, 21);
            this.textboxFirstName.TabIndex = 3;
            // 
            // buttonBack
            // 
            this.buttonBack.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.buttonBack.Location = new System.Drawing.Point(28, 25);
            this.buttonBack.Margin = new System.Windows.Forms.Padding(2);
            this.buttonBack.Name = "buttonBack";
            this.buttonBack.Size = new System.Drawing.Size(68, 28);
            this.buttonBack.TabIndex = 7;
            this.buttonBack.Text = "Back";
            this.buttonBack.UseVisualStyleBackColor = true;
            this.buttonBack.Click += new System.EventHandler(this.buttonBack_Click);
            // 
            // labelViewDetails
            // 
            this.labelViewDetails.AutoSize = true;
            this.labelViewDetails.BackColor = System.Drawing.Color.Transparent;
            this.labelViewDetails.Font = new System.Drawing.Font("Onyx", 48F);
            this.labelViewDetails.Location = new System.Drawing.Point(258, 36);
            this.labelViewDetails.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.labelViewDetails.Name = "labelViewDetails";
            this.labelViewDetails.Size = new System.Drawing.Size(226, 72);
            this.labelViewDetails.TabIndex = 0;
            this.labelViewDetails.Text = "Add Manager";
            // 
            // labelPassword
            // 
            this.labelPassword.AutoSize = true;
            this.labelPassword.BackColor = System.Drawing.Color.Transparent;
            this.labelPassword.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F);
            this.labelPassword.Location = new System.Drawing.Point(231, 177);
            this.labelPassword.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.labelPassword.Name = "labelPassword";
            this.labelPassword.Size = new System.Drawing.Size(92, 24);
            this.labelPassword.TabIndex = 0;
            this.labelPassword.Text = "Password";
            // 
            // textboxPassword
            // 
            this.textboxPassword.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.textboxPassword.Location = new System.Drawing.Point(338, 180);
            this.textboxPassword.Margin = new System.Windows.Forms.Padding(2);
            this.textboxPassword.MaxLength = 32;
            this.textboxPassword.Name = "textboxPassword";
            this.textboxPassword.Size = new System.Drawing.Size(163, 21);
            this.textboxPassword.TabIndex = 2;
            // 
            // comboBoxAccessLevel
            // 
            this.comboBoxAccessLevel.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.comboBoxAccessLevel.FormattingEnabled = true;
            this.comboBoxAccessLevel.Items.AddRange(new object[] {
            "1",
            "2"});
            this.comboBoxAccessLevel.Location = new System.Drawing.Point(338, 298);
            this.comboBoxAccessLevel.Name = "comboBoxAccessLevel";
            this.comboBoxAccessLevel.Size = new System.Drawing.Size(163, 21);
            this.comboBoxAccessLevel.TabIndex = 5;
            // 
            // AdminManagerAdd
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackgroundImage = global::SuperStopNBuy.Properties.Resources.adminBackground;
            this.ClientSize = new System.Drawing.Size(734, 461);
            this.Controls.Add(this.comboBoxAccessLevel);
            this.Controls.Add(this.labelPassword);
            this.Controls.Add(this.textboxPassword);
            this.Controls.Add(this.buttonSaveAndExit);
            this.Controls.Add(this.labelUsername);
            this.Controls.Add(this.textboxUsername);
            this.Controls.Add(this.labelAccessLevel);
            this.Controls.Add(this.labelLastName);
            this.Controls.Add(this.labelFirstName);
            this.Controls.Add(this.textboxLastName);
            this.Controls.Add(this.textboxFirstName);
            this.Controls.Add(this.buttonBack);
            this.Controls.Add(this.labelViewDetails);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Margin = new System.Windows.Forms.Padding(2);
            this.MaximizeBox = false;
            this.Name = "AdminManagerAdd";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Super Stop \'N Buy";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button buttonSaveAndExit;
        private System.Windows.Forms.Label labelUsername;
        private System.Windows.Forms.TextBox textboxUsername;
        private System.Windows.Forms.Label labelAccessLevel;
        private System.Windows.Forms.Label labelLastName;
        private System.Windows.Forms.Label labelFirstName;
        private System.Windows.Forms.TextBox textboxLastName;
        private System.Windows.Forms.TextBox textboxFirstName;
        private System.Windows.Forms.Button buttonBack;
        private System.Windows.Forms.Label labelViewDetails;
        private System.Windows.Forms.Label labelPassword;
        private System.Windows.Forms.TextBox textboxPassword;
        private System.Windows.Forms.ComboBox comboBoxAccessLevel;
    }
}